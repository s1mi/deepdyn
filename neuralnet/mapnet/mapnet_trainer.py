import os

import PIL.Image as IMG
import numpy as np
import torch

from neuralnet.torchtrainer import NNTrainer
from neuralnet.utils.measurements import ScoreAccumulator

sep = os.sep


class ThrnetTrainer(NNTrainer):
    def __init__(self, **kwargs):
        NNTrainer.__init__(self, **kwargs)
        self.patch_shape = self.run_conf.get('Params').get('patch_shape')
        self.patch_offset = self.run_conf.get('Params').get('patch_offset')

    def evaluate(self, data_loaders=None, logger=None, gen_images=False):
        assert (logger is not None), 'Please Provide a logger'
        self.model.eval()

        print('\nEvaluating...')
        with torch.no_grad():
            eval_score = 0.0

            for loader in data_loaders:
                img_obj = loader.dataset.image_objects[0]
                segmented_img = torch.LongTensor(img_obj.working_arr.shape[0],
                                                 img_obj.working_arr.shape[1]).fill_(0).to(self.device)
                gt = torch.LongTensor(img_obj.ground_truth).to(self.device)

                for i, data in enumerate(loader, 1):
                    inputs = data['inputs'].float().to(self.device)
                    labels = data['labels'].float().to(self.device)
                    clip_ix = data['clip_ix'].int().to(self.device)

                    outputs = self.model(inputs)
                    _, predicted = torch.max(outputs, 1)

                    for j in range(predicted.shape[0]):
                        p, q, r, s = clip_ix[j]
                        segmented_img[p:q, r:s] += predicted[j]
                    print('Batch: ', i, end='\r')

                segmented_img[segmented_img > 0] = 255
                # segmented_img[img_obj.mask == 0] = 0

                img_score = ScoreAccumulator()

                if gen_images:
                    img = segmented_img.clone().cpu().numpy()
                    img_score.add_array(img_obj.ground_truth, img)
                    # img = iu.remove_connected_comp(np.array(segmented_img, dtype=np.uint8),
                    #                                connected_comp_diam_limit=10)
                    IMG.fromarray(np.array(img, dtype=np.uint8)).save(
                        os.path.join(self.log_dir, img_obj.file_name.split('.')[0] + '.png'))
                else:
                    img_score.add_tensor(segmented_img, gt)
                    eval_score += img_score.get_prf1a()[2]

                prf1a = img_score.get_prf1a()
                print(img_obj.file_name, ' PRF1A', prf1a)
                self.flush(logger, ','.join(str(x) for x in [img_obj.file_name] + prf1a))

        self._save_if_better(score=eval_score / len(data_loaders))
