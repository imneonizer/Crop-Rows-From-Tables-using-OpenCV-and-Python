#### Crop Cells From Table Images

Hello Folks! this project is based on OpenCV and Python with the following codes you can  automatically crop out Cells / Boxes from image of data tables.

It automatically recognizes horizontal and Vertical lines from images
and Crop Boxes i.e, ( Cells of the given Table in our case).

>simply Run the "crop_boxes.py" and it will crop out each boxes line by line for you cropped out images will be stored in "cropped" directory.

#### Required Modules

`````python
>> pip install opencv-contrib-python
>> pip install numpy
`````

#### Illustrations

> Input Image: ``sample_image.jpg``
>
> ![](sample_image.jpg)



> Detecting Vertical Lines
>
> ![](inter_processing/verticle_lines.jpg)
>
> Detecting Horizontal Lines
>
> ![](inter_processing/horizontal_lines.jpg)
>
> Combined Mask
>
> ![](inter_processing/img_final_bin.jpg)
>
> Final Detected Table
>
> ![](inter_processing/Image_bin.jpg)



#### Output

> All the cropped Boxes / Cells are stored in ``cropped`` Directory
>
> ![](cropped/1.png)
>
> ![](cropped/2.png)
>
> ![](cropped/3.png)
>
> ![](cropped/4.png)
>
> ![](cropped/5.png)
>
> ![](cropped/6.png)
>
> ![](cropped/7.png)
>
> ![](cropped/8.png)
>
> ![](cropped/9.png)
>
> ![](cropped/10.png)

