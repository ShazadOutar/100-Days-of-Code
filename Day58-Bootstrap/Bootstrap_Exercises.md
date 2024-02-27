#### Bootstrap Layout Exercises [Link](https://appbrewery.github.io/bootstrap-layout/)
#### Exercise 1:
- Make the 2 columns 50% on desktop and 100% on mobile
```html
<div class="container">
	<div class="row">
		<div class="col-lg-6 col-sm-12">50% desktop, 100% mobile</div>
	    <div class="col-lg-6 col-sm-12">50% desktop, 100% mobile</div>
	</div>
</div>
```
- On large devices and above, use 50% (6/12 columns) and on small to large use 100% (12/12 columns)
#### Exercise 2:
```html
<!-- Modify the HTML below to make the blue boxes behave like the red ones. -->
<div class="row">
	<div class="col-lg-6 col-sm-12 col-10">Column 1</div>
    <div class="col-lg-3 col-sm-6 col-10">Column 2</div>
    <div class="col-lg-3 col-sm-6 col-10">Column 3</div>
</div>
```
- On large and above split as 6-3-3, on small split 12 and 6-6, finally when it's below small use 10 columns for all
#### Exercise 3:
```html
<!-- Modify the HTML below to make the indigo boxes behave like the blue ones. -->
<div class="row">
	<div class="col-xxl-1 col-xl-2 col-lg-4 col-md-6">Column 1</div>
	<div class="col-xxl-11 col-xl-10 col-lg-8 col-md-6">Column 2</div>
</div>
```
- Specifying a different layout for multiple different sizes