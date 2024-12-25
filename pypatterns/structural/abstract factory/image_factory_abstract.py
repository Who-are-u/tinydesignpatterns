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


class BootImageFactoryHead(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class BootImageFactoryBody(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class crcBootImageFactoryHead(BootImageFactoryHead):
    def create(self):
        pass

class sb3BootImageFactoryHead(BootImageFactoryHead):
    def create(self):
        pass

class containerBootImageFactoryHead(BootImageFactoryHead):
    def create(self):
        pass

class crcBootImageFactoryBody(BootImageFactoryBody):
    def create(self):
        pass

class sb3BootImageFactoryBody(BootImageFactoryBody):
    def create(self):
        pass

class containerBootImageFactoryBody(BootImageFactoryBody):
    def create(self):
        pass

#==============================================

class BootImageFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_boot_image_head(self):
        pass

    @abstractmethod
    def create_boot_image_body(self):
        pass

class crcBootImageFactory(BootImageFactory):
    def create_boot_image_head(self):
        return crcBootImageFactoryHead()

    def create_boot_image_body(self):
        return crcBootImageFactoryBody()

class sb3BootImageFactory(BootImageFactory):
    def create_boot_image_head(self):
        return sb3BootImageFactoryHead()

    def create_boot_image_body(self):
        return sb3BootImageFactoryBody()

class containerBootImageFactory(BootImageFactory):
    def create_boot_image_head(self):
        return containerBootImageFactoryHead()

    def create_boot_image_body(self):
        return containerBootImageFactoryBody()

#client:
    
    boot_image_Factory = crcBootImageFactory()
    boot_image_Factory.create_boot_image_head()
    boot_image_Factory.create_boot_image_body()



