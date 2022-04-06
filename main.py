import os
from PIL import Image


def reshape_and_convert(input_path, output_path, reshape_size: tuple, reduce=False):
    im = Image.open(input_path)
    im = im.resize(reshape_size)
    # if reduce:
    #     im = im.reduce(10)
    #     im = im.resize(reshape_size)
    im.save(output_path)
    print(im.size)


if __name__ == '__main__':
    fig_dir = 'originFig'
    new_fig_dir = 'newFig'
    main_dir = os.path.join(new_fig_dir, "main")
    thubnail_dir = os.path.join(new_fig_dir, "thumbnail")
    os.makedirs(new_fig_dir, exist_ok=True)
    os.makedirs(main_dir, exist_ok=True)
    os.makedirs(thubnail_dir, exist_ok=True)

    requirement = {
        "banner": {"size": (750, 400), "format": '.png'},
        "cover": {"size": (240, 240), "format": '.png'},
        "small": {"size": (50, 50), "format": '.png'},
        "main": {"size": (240, 240), "format": '.gif'},
        "thumbnail": {"size": (120, 120), "format": '.png'},
        "guide": {"size": (750, 560), "format": '.png'},  # set to jpeg due to upload size limit
        "thank": {"size": (750, 750), "format": '.png'}   # set to jpeg due to upload size limit
    }

    img_id = 1
    for im in os.listdir(fig_dir):
        filename = os.path.basename(im).split('.')[0]
        if filename == "banner":
            reshape_and_convert(os.path.join(fig_dir, im),
                                os.path.join(new_fig_dir, "banner" + requirement["banner"]["format"]),
                                reshape_size=requirement["banner"]["size"])
        elif filename == "cover":
            reshape_and_convert(os.path.join(fig_dir, im),
                                os.path.join(new_fig_dir, "cover" + requirement["cover"]["format"]),
                                reshape_size=requirement["cover"]["size"])
        elif filename == "small":
            reshape_and_convert(os.path.join(fig_dir, im),
                                os.path.join(new_fig_dir, "small" + requirement["small"]["format"]),
                                reshape_size=requirement["small"]["size"])
        elif filename == "guide":
            reshape_and_convert(os.path.join(fig_dir, im),
                                os.path.join(new_fig_dir, "guide" + requirement["guide"]["format"]),
                                reshape_size=requirement["guide"]["size"])
        elif filename == "thank":
            reshape_and_convert(os.path.join(fig_dir, im),
                                os.path.join(new_fig_dir, "thank" + requirement["thank"]["format"]),
                                reshape_size=requirement["thank"]["size"])
        else:
            # save main fig
            reshape_and_convert(os.path.join(fig_dir, im),
                                os.path.join(main_dir, f"{img_id}" + requirement["main"]["format"]),
                                reshape_size=requirement["main"]["size"])
            # save thumbnail
            reshape_and_convert(os.path.join(fig_dir, im),
                                os.path.join(thubnail_dir, f"{img_id}" + requirement["thumbnail"]["format"]),
                                reshape_size=requirement["thumbnail"]["size"])
            img_id += 1
