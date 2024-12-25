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
from test_config.image import *



class BootImageFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_boot_image(self):
        pass


class crcBootImageFactory(BootImageFactory):
    @abstractmethod
    def create_boot_image(self):
        return crcBootImage()


class sb3BootImageFactory(BootImageFactory):
    @abstractmethod
    def create_boot_image(self):
        return sb3BootImage()


class containerBootImageFactory(BootImageFactory):
    @abstractmethod
    def create_boot_image(self):
        return containerBootImage()
    

#client:
    
    crcFactoty = crcBootImageFactory()
    bootimage = crcFactoty.create_boot_image()
    bootimage.binary_file
    bootimage.load_address
    bootimage.load_address




