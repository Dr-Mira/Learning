--------------------------------------------------------------------------------------------------
MindCuber-Scrambler
------------------------------------------------------------------------------------------------
How to install:
> 1. Copy the content of the RubiksScrambler.py script into free slot of the hub
> 2. Play

Purpose:      
> Rubiks Scrambler based on David Gilday design MindCuber-RI robot Rubik's Cube solver

Explanation:   
> There are 3 commands defined: one to flip the cube, one to rotate the bottom and one to
> rotate the whole cube. All of them can do clockwise or counterclockwise based on
> their direction parameter (-1 or 1). Those 3 commands are arranged to create moves
> U, D, R, L, F, B, U', D', R', L', F', B', 2U, 2D, 2R, 2L, 2F, and 2B. Algorithm
> then create a sequence of 20 randomly picked moves from this list, and perform these moves.

Notes:   
> Please note that this is not truly random but a pseudo-random, as sequence is generated with
> Python random module.

> This script do not mimic wide moves (u, d, r, l, f, b) and slice moves (M, E, S)

> All moves are relative to the cube position from previous step. 
> In other words, if you use commercial cube scrambler it will scramble differently for same sequence. 
> This is because the robot can rotate only the bottom piece, thus we are saving time not to move cube to its 
> staring position after each move (yellow up, blue forward, red right).

> Lastly, there is room for optimization, for example sometimes the robot
> perform 2 consecutive U2.

> You can play with the script as you please. Enjoy.
---------------------------------------------------------------------------------------------------
Formal:

> - Author:       
> Mira Kaspar, David Gilday
> - Version:      
> v1p0
> - Copyright:    
> (C) 2022 Mira Kaspar
> - Website:      
>http://mindcuber.com
> - Usage:        
>This software may be used for any non-commercial purpose providing
>that the authors David Gilday and Mira Kaspar are acknowledged.
> - Disclaimer:   
> I am author of this script, but David is true mind behind the robot design and solver algorithm.
> This software is provided 'as is' without warranty of any kind, either
> express or implied, including, but not limited to, the implied warranties
> of fitness for a purpose, or the warranty of non-infringement.
---------------------------------------------------------------------------------------------------
