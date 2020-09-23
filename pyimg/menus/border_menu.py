import os
from tkinter import Menu

from pyimg.config import constants
from pyimg.menus.operation_interface import (BinaryImageOperation,
                                             UnaryImageOperation,
                                             UnaryWithParamsImageOperation)
from pyimg.models.image import ImageImpl, border_detection , operators
from pyimg.modules.image_io import display_img, save_img


def linear_adj_image_wrapper(image: ImageImpl):
    adjusted_img = operators.linear_adjustment(image)
    img = adjusted_img.convert_to_pil()
    display_img(img)
    save_img(img, os.path.join(constants.SAVE_PATH, "result_img.jpg"))


class BorderMenu:
    """
    This class is a simple wrapper around tkinter menu object.
    it's self display as a menu in the top bar.
    """

    def __init__(self, menubar, image_io):
        filter_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Border Detection", menu=filter_menu)

        filter_menu.add_command(
            label="Prewitt operator",
            command=UnaryWithParamsImageOperation(
                image_io,
                'Prewitt',
                lambda image: linear_adj_image_wrapper(
                    border_detection.prewitt_detector(image)
                ),
                params=[],
            ).generate_interface,
        )
