This tool lets you create and manipulate custom walls for Beat Saber.

On the left textfield (Input) you can enter a json fragment containing existing walls, which can then be manipulated.
After inserting json data press "Read Json".
All results will be displayed on the right textfield (Output).

The values below "Data" show the first/selected wall read from the json. 
Otherwise they can be used to create a new wall with "Add New Wall".
New walls will be stacked up on old walls.
"Delete Wall" will delete the currently selected (displayed in "Data") wall.

"Forth" and "Back" lets you navigate through all current walls. The selected wall shows its data in the fields below "Data".
When a slected wall shall be changed, the value can simply be changed. Afterwards press "Conform Changes".

"Shift/Steps" lets you manipulate existing walls. All values below indicate changes that will be made. "Shift" moves all walls by these values.
"Increase step-by-step" takes all walls (currently displayed in "Output") and changes them as often as "Steps" indicates by these values.
"Mirror" moves all walls to the other side in the map (like MM mirror).
"+Mirror" and "+Shift" does the same as above, but instead of replacing old walls, it adds them on top of it. So you have old and shifted/mirrored walls.

"Clear All" deletes all current walls.

Examples:

Fill Data and press "Add New Wall" to create the new wall. Press "Add New Wall" 5 times to have 5 same walls.
Press "Back" twice, change the Height and press "Confirm Changes" to alter the third wall (displayed now in Output).

Enter a value for "Time" and press "Shift" to change all 5 walls by this value.
Press "Shift+" and you have the once shifted 5 walls and additional 5 walls which were shifted twice.
Enter a value for "Steps" and a value for "LineIndex". All walls (except the original 10) will be increased by LineIndex as much as "Steps"-times.
So with "Steps"=2 there will be 30 walls now. 10 Original, 10 increased once, 10 increased twice.

Number Logic:

The original calculation by Kyle (https://github.com/Kylemc1413/MappingExtensions) is complicated.
This tools makes it a lot easier:
lineindex: 0 is leftmost, 4 is rightmost for 4 lanes play area
height: 1 is a wall of full height, 0.5 a half wall, 0 is a flat wall
start height: according to height, 1 starts on top of a wall with height 1.
width: 1 is a wall of 1 row width, 0 is a thin wall

0 height/width wall have "dark textures" to make the thinnest wall, that still looks like a wall use 0.001
This tool automatically includes shifts by 1000 and the skip from -1000 lineindex to 1000 to make it easy to work with.
