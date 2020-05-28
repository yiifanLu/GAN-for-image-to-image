# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:32:59 2020

@author: 82158
"""

import logging
logger = logging.getLogger('base')


def create_model(opt):
    model = opt['model']
    if model =="GIGAN":
        from .GIGAN_Model import GIGAN_Model as M 
# =============================================================================
#     if model == "resnet":
#         from .Seperate_Denoise_Resnet_model import Seperate_Denoise_Resnet_Model as M 
#     elif model == "seperate_cfm_gan":
#         from .Seperate_Denoise_CFM_model import Seperate_Denoise_CFM_Model as M
#     else:
# =============================================================================
    else:
        raise NotImplementedError('Model [{:s}] not recognized.'.format(model))
    m = M(opt)
    logger.info('Model [{:s}] is created.'.format(m.__class__.__name__))
    return m
