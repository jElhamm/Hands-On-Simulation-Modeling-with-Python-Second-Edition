# *************************************************************************************************
#                                                                                                 *
#                Hands On Simulation Modeling with Python - Chapter 3                             *
#                                                                                                 *
#       This code defines a class ImageAugmentor for augmenting images using TensorFlow's         *
#       ImageDataGenerator. The class takes an image file path and an optional save directory     *
#       as inputs. It applies a series of augmentations including rotation, width and height      *
#       shifts, shear, zoom, and horizontal flipping to generate augmented versions of the        *
#       original image.                                                                           *
#                                                                                                 *
#       The _create_save_dir method ensures that the specified directory for saving augmented     *
#       images exists. The load_and_preprocess_image method loads the image from the provided     *
#       path, converts it to a format suitable for augmentation, and handles file not found       *
#       errors. The augment_and_save_images method generates and saves a specified number of      *
#       augmented images with a given prefix and format.                                          *
#                                                                                                 *
# *************************************************************************************************


import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class ImageAugmentor:
    def __init__(self, img_path, save_dir='AugImage'):
        self.img_path = img_path
        self.save_dir = save_dir
        self.image_generation = ImageDataGenerator(
            rotation_range=10,
            width_shift_range=0.1,
            height_shift_range=0.1,
            shear_range=0.1,
            zoom_range=0.1,
            horizontal_flip=True,
            fill_mode='nearest'
        )
        self._create_save_dir()

    def _create_save_dir(self):
        """Create the directory for saving augmented images if it doesn't exist."""
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def load_and_preprocess_image(self):
        """Load the image and preprocess it to be ready for augmentation."""
        try:
            source_img = load_img(self.img_path)
            x = img_to_array(source_img)
            x = x.reshape((1,) + x.shape)
            return x
        except FileNotFoundError:
            print(f"Error: The image at path '{self.img_path}' was not found.")
            return None

    def augment_and_save_images(self, batch_size=1, num_images=50, save_prefix='new_image', save_format='jpeg'):
        """Generate and save augmented images."""
        x = self.load_and_preprocess_image()
        if x is None:
            return

        i = 0
        for batch in self.image_generation.flow(x, batch_size=batch_size,
                                                save_to_dir=self.save_dir,
                                                save_prefix=save_prefix,
                                                save_format=save_format):
            i += 1
            if i >= num_images:
                break
        print(f"{num_images} augmented images have been saved to '{self.save_dir}'.")


# Example of using the class
augmentor = ImageAugmentor(img_path='Test_Image.jpg', save_dir='AugImage')
augmentor.augment_and_save_images(num_images=50)
