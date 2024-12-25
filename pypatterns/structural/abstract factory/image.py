#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author   : Jianping Zhang
# @Date     : 2023-12-07 14:31
# @Last Modified by : Jianping Zhang
# @Last Modified time : 2023-12-07 14:31
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"../../../"))
from rom_utils.helper.misc import create_file_path
from abc import ABCMeta, abstractproperty, abstractmethod
from rom_utils.imggen.ahab import AHABImageGen
from rom_utils.imggen.ahab import AHABEncryption
from rom_utils.imggen.ahab import AHABCipherMode
from rom_utils.keys_certs import AHABKeysCerts



class BootImage(metaclass=ABCMeta):
    @abstractproperty
    def load_address(self):
        pass

    @abstractproperty
    def binary_file(self):
        pass
    
    @abstractproperty
    def rkth(self):
        pass


class crcBootImage(BootImage):
    """ 
    """
    def __init__(self, **kwargs):
        pass
        
    @property
    def load_address(self):
        pass

    @property
    def binary_file(self):
        pass
    
    @property
    def rkth(self):
        pass
    

class sb3BootImage(BootImage):
    """ 
    """
    def __init__(self, **kwargs):
        pass
        
    @property
    def load_address(self):
        pass

    @property
    def binary_file(self):
        pass
    
    @property
    def rkth(self):
        pass


class containerBootImage(BootImage):
    """ 
    """
    def __init__(self, **kwargs):
        pass
        
    @property
    def load_address(self):
        pass

    @property
    def binary_file(self):
        pass
    
    @property
    def rkth(self):
        pass
