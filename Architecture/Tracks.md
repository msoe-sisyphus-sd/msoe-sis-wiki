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

 