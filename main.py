"""
Author: Sanidhya Mangal
GitHub: sanidhyamangal
email: mangalsanidhya19@gmail.com
"""
import tensorflow as tf

def train_model(namescope:str, dense_units:int) -> None:

    image_data = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True
    )

    train_data = image_data.flow_from_directory(f'{namescope}_train/', target_size=(150, 150), batch_size=32, color_mode='rgb')
    val_data = image_data.flow_from_directory(f'{namescope}_test/', target_size=(150, 150), batch_size=32, color_mode='rgb')

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu', input_shape=(150, 150 ,3)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(rate=0.4),
        tf.keras.layers.Dense(dense_units)
    ])

    model.compile(optimizer = tf.keras.optimizers.RMSprop(lr=1e-4),
                loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    print(f"Model for {namescope}\n",model.summary())

    tensorboard = tf.keras.callbacks.TensorBoard(log_dir=f'./{namescope}', histogram_freq=1)

    model.fit_generator(train_data, epochs=100, callbacks=[tensorboard], validation_data=val_data)

    print(f"saving model for {namescope}")
    model.save(f'{namescope}.h5')

train_model(namescope="lung", dense_units=3)
