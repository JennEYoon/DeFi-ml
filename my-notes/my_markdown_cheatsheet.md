#  My Markdown Cheatsheet  

#### Author: Jennifer E. Yoon  

#### Tasks for 8/24/2019 2:00 AM    

This is an unordered list. Use one space, * , one space.
 * one
 * two
 * three

This is an ordered list.  Use one space, 1. , one space.
 1. Link to SEC Edgar data source
 1. Link to various Stress Test Results  
 1. Link to leverage ratios, and systemic risk calculation 
 1. Link to credit risk data sources 
 1. Link to Energy Derivatives data source [EIA.gov](https://www.eia.gov/)  

HTML links to external and Github relative pages. 
> [Link to projects.html](http://datasciY.com/projects.html) Place holder for project webpages.  
  ```[Link](http://datasciY.com/projects.html) Place holder for project webpages.```
  
> [I'm an inline-style link with title](https://www.google.com "Google's Homepage")  
  ```[I'm an inline-style link with title](https://www.google.com "Google's Homepage")```
  
> [I'm a relative reference to a repository file](../master/README.md)  
  ```[I'm a relative reference to a repository file](../master/README.md)```

Code block and quote block.  

    Use ``` three tick-marks before and after for all code block.  
    Use single ` tick-mark before and after for `inline code` format.
    Use > for all quote blocks.
    Can also indent 4 spaces for quote blocks.

Insert Image  
 
 ```html
 <img src="url" alt="alt text" width="whatever" height="whatever">
 ![image link](https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png)
 Markdown image codes on Github can **no longer** resize image.
 ```
 
Link to Google Drive Image: https://drive.google.com/file/d/1wShQ5PbP_AMeZQbS7l0x0Q_63jQlhTSi/view?usp=sharing  
 
**Insert local image, resize with html:**  
html code: `<img src="../main/jennifer_lawrence_bobcut.png" alt="Jennifer Lawrence" width="250">`  

<img src="../main/jennifer_lawrence_bobcut.png" alt="Jennifer Lawrence" width="250">


**Insert with markdown, no resizing:**  
markdown code: `![test image size](../main/jennifer_lawrence_bobcut.png)`  
![test image size](../main/jennifer_lawrence_bobcut.png)
 
 **Image with margins and center alignment:**  

```html
https://www.w3schools.com/tags/smiley.gif
<p><img src="smiley.gif" alt="Smiley face" width="42" height="42" align="middle" style="margin:50px 10px">
This is some text.  This is some text. This is some text.</p>
```

<p><img src="https://www.w3schools.com/tags/smiley.gif" alt="Smiley face" width="42" height="42" align="middle" style="margin:50px 10px" />This is some text. This is some text. This is some text.</p>

**HTML image margins ignored.**   
The image alignment is for vertical vis-a-vis paragraph text, top, middle, bottom.    
Only "paragraph margins or align" work, but need some text to apply style.  

<p style="margin: 16px">This is "margin left" text. <img src="https://www.w3schools.com/tags/smiley.gif" alt="Smiley face" width="42" height="42" align="middle" style="margin:50px 10px" />This is some text. This is some text.</p>

<p align="center">This is "align center" text. <img src="https://www.w3schools.com/tags/smiley.gif" alt="Smiley face" width="42" height="42" align="middle" style="margin:50px 10px" />This is some text. This is some text.</p>
