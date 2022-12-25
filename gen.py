from trdg import string_generator
from trdg.generators import from_strings
import os
from trdg.data_generator import FakeTextDataGenerator
from trdg.utils import load_fonts

VIN_CHARS = '0123456789ABCDEFGHJKLMNPRSTUVWXYZ'
SIGN_CHARS = '0123456789АВЕКМНОРСТУХ'




def gen_1():
    vin_strings = string_generator.create_strings_randomly(
                                                        length=1,
                                                        allow_variable=False,
                                                        count=10,
                                                        lang='en',
                                                        chars=VIN_CHARS,
                                                        let=True,
                                                        num=False,
                                                        sym=False,
                                                        sign=False
                                                    )
    print(vin_strings)
    generator = from_strings.GeneratorFromStrings(
                                    strings=vin_strings,
                                    count=10,
                                    fonts = [],
                                    language= "en",
                                    size = 32,
                                    skewing_angle = 0,
                                    random_skew = False,
                                    blur = 0,
                                    random_blur = False,
                                    background_type = 0,
                                    distorsion_type = 0,
                                    distorsion_orientation = 0,
                                    is_handwritten = False,
                                    width = -1,
                                    alignment = 1,
                                    text_color = "#282828",
                                    orientation = 0,
                                    space_width = 1.0,
                                    character_spacing = 0,
                                    margins = (5, 5, 5, 5),
                                    fit = False,
    #                                name_format = 2,
                                    output_mask = False,
                                    word_split = False,
                                    image_dir = os.path.join(
                                        "..", os.path.split(os.path.realpath(__file__))[0], "images"
                                    ),
                                    stroke_width = 0,
                                    stroke_fill = "#282828",
                                    image_mode = "RGB",
                                    output_bboxes = 3,
                                    yolo_classes = dict((i, j) for j, i in enumerate(VIN_CHARS)),
                                    rtl = False,
                                )

if __name__ == '__main__':
    fonts = load_fonts('ru')
    for i, font in enumerate(fonts):
        FakeTextDataGenerator.generate(
            index=i,
            text=SIGN_CHARS,
            font=font,
            out_dir='generated',
            size=32,
            extension='jpg',
            skewing_angle=0,
            random_skew=False,
            blur=0,
            random_blur=False,
            background_type=3,
            distorsion_type=3,
            distorsion_orientation=0,
            is_handwritten=False,
            name_format=3,
            width=-1,
            alignment=1,
            text_color = "#282828",
            orientation=0,
            space_width=1,
            character_spacing=0,
            margins= (5, 5, 5, 5),
            fit=False,
            output_mask=False,
            word_split=False,
            image_dir = "trdg/images",
            stroke_width=0,
            stroke_fill= "#282828",
            image_mode= "RGB",
            output_bboxes=3,
            yolo_classes=dict((i, j) for j, i in enumerate(SIGN_CHARS))
            )
