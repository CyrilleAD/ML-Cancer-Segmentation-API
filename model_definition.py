import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, Conv2DTranspose, MaxPooling2D, Concatenate, Cropping2D, Dropout
from tensorflow.keras.models import Model

class SegmentationModel(tf.keras.Model):
    def __init__(self):
        super(SegmentationModel, self).__init__()
        
        # Encoder
        self.conv1_1 = Conv2D(64, 3, activation='relu', padding='same')
        self.conv1_2 = Conv2D(64, 3, activation='relu', padding='same')
        self.pool1 = MaxPooling2D(pool_size=(2, 2))
        
        self.conv2_1 = Conv2D(128, 3, activation='relu', padding='same')
        self.conv2_2 = Conv2D(128, 3, activation='relu', padding='same')
        self.pool2 = MaxPooling2D(pool_size=(2, 2))
        
        self.conv3_1 = Conv2D(256, 3, activation='relu', padding='same')
        self.conv3_2 = Conv2D(256, 3, activation='relu', padding='same')
        self.pool3 = MaxPooling2D(pool_size=(2, 2))
        
        self.conv4_1 = Conv2D(512, 3, activation='relu', padding='same')
        self.conv4_2 = Conv2D(512, 3, activation='relu', padding='same')
        self.drop4 = Dropout(0.5)
        self.pool4 = MaxPooling2D(pool_size=(2, 2))
        
        # Bottleneck
        self.conv5_1 = Conv2D(1024, 3, activation='relu', padding='same')
        self.conv5_2 = Conv2D(1024, 3, activation='relu', padding='same')
        self.drop5 = Dropout(0.5)
        
        # Decoder
        self.up6 = Conv2DTranspose(512, 2, strides=(2, 2), padding='same')
        self.conv6_1 = Conv2D(512, 3, activation='relu', padding='same')
        self.conv6_2 = Conv2D(512, 3, activation='relu', padding='same')
        
        self.up7 = Conv2DTranspose(256, 2, strides=(2, 2), padding='same')
        self.conv7_1 = Conv2D(256, 3, activation='relu', padding='same')
        self.conv7_2 = Conv2D(256, 3, activation='relu', padding='same')
        
        self.up8 = Conv2DTranspose(128, 2, strides=(2, 2), padding='same')
        self.conv8_1 = Conv2D(128, 3, activation='relu', padding='same')
        self.conv8_2 = Conv2D(128, 3, activation='relu', padding='same')
        
        self.up9 = Conv2DTranspose(64, 2, strides=(2, 2), padding='same')
        self.conv9_1 = Conv2D(64, 3, activation='relu', padding='same')
        self.conv9_2 = Conv2D(64, 3, activation='relu', padding='same')
        
        # Output layer
        self.conv10 = Conv2D(6, 1, activation='softmax')
        
    def call(self, inputs):
        # Encoder
        conv1 = self.conv1_1(inputs)
        conv1 = self.conv1_2(conv1)
        pool1 = self.pool1(conv1)
        
        conv2 = self.conv2_1(pool1)
        conv2 = self.conv2_2(conv2)
        pool2 = self.pool2(conv2)
        
        conv3 = self.conv3_1(pool2)
        conv3 = self.conv3_2(conv3)
        pool3 = self.pool3(conv3)
        
        conv4 = self.conv4_1(pool3)
        conv4 = self.conv4_2(conv4)
        drop4 = self.drop4(conv4)
        pool4 = self.pool4(drop4)
        
        # Bottleneck
        conv5 = self.conv5_1(pool4)
        conv5 = self.conv5_2(conv5)
        drop5 = self.drop5(conv5)
        
        # Decoder
        up6 = self.up6(drop5)
        merge6 = Concatenate()([drop4, up6])
        conv6 = self.conv6_1(merge6)
        conv6 = self.conv6_2(conv6)
        
        up7 = self.up7(conv6)
        merge7 = Concatenate()([conv3, up7])
        conv7 = self.conv7_1(merge7)
        conv7 = self.conv7_2(conv7)
        
        up8 = self.up8(conv7)
        merge8 = Concatenate()([conv2, up8])
        conv8 = self.conv8_1(merge8)
        conv8 = self.conv8_2(conv8)
        
        up9 = self.up9(conv8)
        merge9 = Concatenate()([conv1, up9])
        conv9 = self.conv9_1(merge9)
        conv9 = self.conv9_2(conv9)
        
        # Output
        conv10 = self.conv10(conv9)
        
        return conv10
    
    def build_model(self):
        inputs = Input(shape=(256, 256, 3))
        outputs = self.call(inputs)
        return Model(inputs=inputs, outputs=outputs)