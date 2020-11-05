# Theta-Rho Tracks

Tracks are composed of a series of points in polar coordinates (theta, rho) which map to a specific point on the table.

Theta is in radians and ranges from -Inf < theta < +Inf

Rho is an unit-less value and ranges from 0 <= rho <= 1
* 0 is the center of the table and 1 is the outer edge

The file may have a header commented with the `#` character but these lines are ignored and have no bearing in execution or as metadata.

Theta and Rho are separated by spaces.
Points are separated by new lines (`\n`)

## Example
```
# this is a comment
0 0
6.2 1
```

## Drawing
The table with draw an arc between two points meaning that if they are far enough away as the table moves the ball it will draw an arc rather than a straight line between them. This is sometimes desirable (see the erase track at `sisbot/content/tracks/2CBDAE96-EC22-48B4-A369-BFC624463C5F.thr) but for capturing linear lines more points are needed as to reduce the arc and simulate a straight line between the two points.

## Creating Tracks and Mapping from Rectangular (x,y) Space
Refer to this [community forum post](https://sisyphus-industries.com/community/community-tracks/sisyphus-programming-guide-so-far/)
* In case the link is dead here is an archived version of the document: [1567911970-sisyphus-table-programming-logic-1.docx](uploads/0f322664dd7a1ab1235a3967eebba4cc/1567911970-sisyphus-table-programming-logic-1.docx)

## Lateral Erase Track
To create the lateral erase track @burkhardtr decided to be lazy and write a program to auto-generate the file for him. It is a bit hacky so be kind but it can be reused to convert other rectangular space 

### Warnings
@burkhardtr is pretty sure the only reason this file produces correct output is due to the way lines are partitioned. Essentially the track will always cross from +y to -y on the left side of the y-axis. The track crosses the x-axis moving from Quadrant II to Quadrant III. If the ball were to cross from Quadrant I to Quadrant IV then there would need to be a bit of logic to re-align the ball so it doesn't jump when moving over the y-axis in the second half of the track's run.

### Auto-Generating File
[main.py](uploads/76c64739cbacf80d5c4a793985cc2cac/main.py)

#### Steps to Use
Requirements: Python 3+, matplotlib (can be downloaded with `pip`)
`python main.py`

#### Concessions
This file is not perfect - there are swaths of commented code and it could be organized a lot better but this was meant as a quick dirty approach rather than writing a file by hand.

## Getting a Track on the Table

Summary: HTTP POST to `/sisbot/add_track` 

### What @burkhardtr Did (2020-11-05)
1. Use the auto generating file to create a .thr
2. Edit the file removing newlines and adding `\n` literals between points
3. Open this [Postman](https://www.postman.com/downloads/) config [sisbot.postman_collection.json](uploads/a78701463961fd47a23b045eb3582c9b/sisbot.postman_collection.json)
4. Select the **add_track** method
5. Change the body contents selecting a new id, name, and copy-paste the edited .thr data into the `verts` attribute
6. Post
7. Select the **set_track** method
8. Change the body contents by inserting the new id and name from step 5
9. Post
10. Watch the table go!!

 