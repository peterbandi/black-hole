"""Try different image reader backeds."""

from pathlib import Path

from aiosynimage import ImageReader, SpacingValidator


def metadata(image_reader: ImageReader) -> dict:
    """Get the metadata from an image."""

    return {
        "format": image_reader.format,
        "coding": image_reader.coding,
        "channels": image_reader.channels,
        "dtype": image_reader.dtype.name,
        "count": image_reader.count,
        "pyramid": [info.__dict__ for info in image_reader.pyramid],
    }

def main():
    """Experiment entry point."""

    data_root = Path("/home/peter/projects/aiosyn-image/tests/data")

    ndpi_path = data_root / "image_a.ndpi"
    ndpi_image = ImageReader(path=ndpi_path, validator=SpacingValidator(isotropic_tolerance=0.005))
    ndpi_meta = metadata(image_reader=ndpi_image)
    print(ndpi_meta)

    svs_path = data_root / "image_b.svs"
    svs_image = ImageReader(path=svs_path)
    svs_meta = metadata(image_reader=svs_image)
    print(svs_meta)

    dicom_path = data_root / "image_c"
    dicom_image = ImageReader(path=dicom_path)
    dicom_meta = metadata(image_reader=dicom_image)
    dicom_patch = dicom_image.read(spacing=32.0, row=340, col=-40, height=400, width=1200)
    print(dicom_meta)

    mrxs_path = data_root / "image_e" / "image_e.mrxs"
    mrxs_image = ImageReader(path=mrxs_path)
    mrxs_meta = metadata(image_reader=mrxs_image)
    mrxs_image.read(spacing=16.0, row=1110, col=2310, height=240, width=250)
    print(mrxs_meta)

    tiff_1_path = data_root / "image_d_0.tif"
    tiff_1_image = ImageReader(path=tiff_1_path)
    tiff_1_meta = metadata(image_reader=tiff_1_image)
    print(tiff_1_meta)

    tiff_2_path = data_root / "image_d_1.tif"
    tiff_2_image = ImageReader(path=tiff_2_path)
    tiff_2_meta = metadata(image_reader=tiff_2_image)
    print(tiff_2_meta)

    tiff_3_path = data_root / "image_d_2.tif"
    tiff_3_image = ImageReader(path=tiff_3_path)
    tiff_3_meta = metadata(image_reader=tiff_3_image)
    print(tiff_3_meta)

    jpeg_path = data_root / "image_f.jpeg"
    jpeg_image = ImageReader(path=jpeg_path, spacing=(0.8, 0.8))
    jpeg_meta = metadata(image_reader=jpeg_image)
    print(jpeg_meta)

    print("Done")


if __name__ == "__main__":
    main()
