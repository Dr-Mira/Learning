
<p><em>Note:<br>
Before you start this project, it's better to get familiar with the basic domino rules. Keep in mind that there are many versions of the game. The rules used in this particular project will be described as we go along.</em></p>

<p>As you might know, a domino is a playing piece that is characterized by the two numbers written on it. The numbers are integers and can range from 0 to 6. A single domino piece has no orientation, so, a full domino set (that includes all the possible pairs of numbers) will have 28 unique dominoes.</p>

<p>You may think that there should be 7*7=49 dominoes in total. However, this is not the case because the combinations like <samp>[1,2]</samp> and <samp>[2,1]</samp> are the same domino, not two separate ones.</p>



<h1>Stage 1</h1>

<p>To play domino, you need a full domino set and at least two players. In this project, the game is played by you and the computer.</p>

<p>At the beginning of the game, each player is handed 7 random domino pieces. The rest are used as stock (the extra pieces).</p>

<p>To start the game, players determine the starting piece. The player with the highest domino or the highest double (<samp>[6,6]</samp> or <samp>[5,5]</samp> for example) will donate that domino as a starting piece for the game. After doing so, their opponent will start the game by going first. If no one has a double domino, the pieces are reshuffled and redistributed.</p>

<p><div class="alert alert-primary"> Status is the player, who is to make the next move </div></p>

<h5>Objective 1</h5>

<ol>
	<li>Generate a full domino set. Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.<br>
	 </li>
	<li>Split the full domino set between the players and the stock by random. You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).<br>
	 </li>
	<li>Determine the starting piece and the first player. Modify the parts accordingly. You should get four parts with domino pieces and one string indicating the player that goes first: either <code class="language-python">"player"</code> or <code class="language-python">"computer"</code>.
	<pre><code class="language-python">Stock pieces      # 14 domino elements
Computer pieces   # 7 or 6 domino elements
Player pieces     # 6 or 7 domino elements
Domino snake      # 1 starting domino
Status            # the player that goes first</code></pre>
	If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3).<br>
	 </li>
	<li>Output all five variables.</li>
</ol>

<p><strong>Example 1</strong></p>

<p><em>The player makes the first move.</em></p>

<pre><code class="language-no-highlight">Stock pieces: [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]]
Computer pieces: [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3]]
Player pieces: [[0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6]]
Domino snake: [[6, 6]]
Status: player</code></pre>

<p><br>
<strong>Example 2</strong></p>

<p><em>The computer makes the first move.</em></p>

<pre><code class="language-no-highlight">Stock pieces: [[2, 6], [3, 4], [5, 6], [0, 5], [1, 2], [4, 6], [2, 3], [0, 6], [0, 0], [6, 6], [2, 4], [2, 2], [0, 1], [3, 3]]
Computer pieces: [[0, 2], [3, 6], [4, 4], [3, 5], [1, 5], [0, 3], [2, 5]]
Player pieces: [[1, 3], [1, 4], [4, 5], [1, 6], [1, 1], [0, 4]]
Domino snake: [[5, 5]]
Status: computer</code></pre>



<h1>Stage 2</h1>

<p>A good game needs a good interface. In this stage, you will make your output user-friendly.</p>

<p>The player should be able to see the domino snake, the so-called playing field, and their own pieces. It's a good idea to enumerate these pieces because throughout the game the player will be selecting them to make a move.</p>

<p>Two things must remain hidden from the player: the stock pieces and the computer's pieces. The player should not be able to see them, only the number of pieces remaining.</p>

<p><strong>Objectives</strong></p>

<ol>
	<li>Print the header using seventy equal sign characters (<code class="java">=</code>).</li>
	<li>Print the number of dominoes remaining in the stock – <code class="java">Stock size: [number]</code>.</li>
	<li>Print the number of dominoes the computer has – <code class="java">Computer pieces: [number]</code>.</li>
	<li>Print the domino snake. At this stage, it consists of the only starting piece.</li>
	<li>Print the player's pieces, <code class="java">Your pieces:</code>, and then one piece per line, enumerated.</li>
	<li>Print the status of the game:<br>
	If <code class="java">status = "computer"</code>, print <code class="java">"Status: Computer is about to make a move. Press Enter to continue..."</code><br>
	If <code class="java">status = "player"</code>, print <code class="java">"Status: It's your turn to make a move. Enter your command."</code><br>
	Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.</li>
</ol>

<p><strong>Example 1</strong></p>

<p><em>The player makes the first move (status = "player")</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.</code></pre>

<p><br>
<strong>Example 2</strong></p>

<p><em>The Computer makes the first move (status = "computer")</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 14
Computer pieces: 7

[5, 5]

Your pieces:
1:[1, 3]
2:[1, 4]
3:[4, 5]
4:[1, 6]
5:[1, 1]
6:[0, 4]

Status: Computer is about to make a move. Press Enter to continue...</code></pre>



<h1>Stage 3</h1>

<p>It's time to bring the game to life. In this stage, you need to add a game loop that will allow players to take turns until the end-game condition is met.</p>

<p>In dominoes, you can make a move by taking one of the following actions:</p>

<ul>
	<li>Select a domino and place it on the right side of the snake.</li>
	<li>Select a domino and place it on the left side of the snake.</li>
	<li>Take an extra piece from the stock (if it's not empty) and skip a turn.</li>
</ul>

<p>To make a move, the player has to specify the action they want to take. In this project, the actions are represented by integer numbers in the following manner: <code class="java">{side_of_the_snake (+/-), domino_number (integer)}</code> or <code class="java">{0}</code>. For example:<br>
<code class="java">-6</code> : Take the sixth domino and place it on the left side of the snake. <br>
<code class="java"> 6</code> : Take the sixth domino and place it on the right side of the snake.<br>
<code class="java"> 0</code> : Take an extra piece from the stock (if it's not empty) and skip a turn or simply skip a turn if the stock is already empty by this point.</p>

<p>When it's time for the player to make a move, your program must prompt the user for a number. If this number exceeds the limitations (larger than the number of dominoes), your program must generate an error message and prompt for input again. Once the valid input is received, your program must apply the move.</p>

<p>For now, don't bother about the AI, our goal is just to make the game playable. So, when it's time for the computer to make a move, make it choose a random number between <code class="java">-computer_size</code> and <code class="java">computer_size</code> (where the <code class="java">computer_size</code> is the number of dominoes the computer has).</p>

<p>The end-game condition can be achieved in two ways:</p>

<ol>
	<li>One of the players runs out of pieces. The first player to do so is considered a winner.</li>
	<li>
	<p>The numbers on the ends of the snake are identical and appear within the snake 8 times. For example, the snake below will satisfy this condition:<br>
	<code class="java"><samp>[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,6],[6,5]</samp></code><br>
	These two snakes, however, will not:<br>
	<code class="java">[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5]</code><br>
	<code class="java">[6,5],[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,1]</code><br>
	If this condition is satisfied, it is no longer possible to go on with this snake. Even after emptying the stock, no player will have the necessary piece. Essentially, the game has come to a permanent stop, so we have a draw.</p>
	</li>
</ol>

<p>When the game ends, your program should print the result.</p>

<p>Throughout the gameplay, the snake will grow in length. If it gets too large, the interface might get ugly. To avoid this problem, draw only the first and the last three pieces of the snake, separate them by three dots, <code class="java">...</code>, for example, <code class="java">[3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4]</code>.</p>

<p><strong>Objectives</strong></p>

<p>Modify your Stage 2 code:</p>

<ol>
	<li>
	<p>At the end of the game, print one of the following phrases:<br>
	<code class="java">Status: The game is over. You won!</code><br>
	<code class="java">Status: The game is over. The computer won!</code><br>
	<code class="java">Status: The game is over. It's a draw!</code></p>
	</li>
	<li>
	<p>Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.</p>
	</li>
	<li>
	<p>Add a game loop that will repeat the following steps until the game ends:</p>
	</li>
</ol>

<ul>
	<li>
	<p>Display the current playing field (stage 2).</p>
	</li>
	<li>
	<p>If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (a not-integer or it exceeds limitations), request a new input with the following message: <code class="java">Invalid input. Please try again.</code>.</p>
	</li>
	<li>
	<p>If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.</p>
	</li>
	<li>
	<p>Switch turns.</p>
	</li>
</ul>

<p>Keep in mind that at this stage we have no rules! Both the player and the computer can place their dominoes however they like.</p>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1</strong></p>

<p><em>Typical gameplay.</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
&gt; 4
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][4, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: Computer is about to make a move. Press Enter to continue...
&gt;
======================================================================
Stock size: 14
Computer pieces: 5

[6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: It's your turn to make a move. Enter your command.
&gt; -6
======================================================================
Stock size: 14
Computer pieces: 5

[1, 6][6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
&gt;
======================================================================
Stock size: 13
Computer pieces: 6

[1, 6][6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]

Status: It's your turn to make a move. Enter your command.
&gt; 0
======================================================================
Stock size: 12
Computer pieces: 6

[1, 6][6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[2, 3]

Status: Computer is about to make a move. Press Enter to continue...
&gt;</code></pre>

<p> </p>

<p><strong>Example 2</strong></p>

<p><em>Invalid input.</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 14
Computer pieces: 5

[4, 4][2, 3][3, 4]

Your pieces:
1:[1, 2]
2:[2, 6]
3:[0, 4]
4:[5, 6]
5:[2, 5]
6:[2, 4]

Status: It's your turn to make a move. Enter your command.
&gt; Hello
Invalid input. Please try again.
&gt;</code></pre>

<p><strong>Example 3</strong></p>

<p><em>Mid-game example. The "domino snake" exceeds six dominoes in length.</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 7
Computer pieces: 4

[6, 6][6, 3][3, 0]...[4, 2][2, 3][3, 6]

Your pieces:
1:[0, 0]
2:[1, 2]
3:[5, 5]

Status: It's your turn to make a move. Enter your command.</code></pre>

<p><strong>Example 4</strong></p>

<p><em>The player wins.</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4]

Your pieces:
1:[4, 4]

Status: It's your turn to make a move. Enter your command.
&gt; 1
======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[0, 3][3, 4][4, 4]

Your pieces:

Status: The game is over. You won!</code></pre>



<h1>Stage 4</h1>

<p>You can't have a game without rules. It's time to introduce them!</p>

<p>Until now, the players were able to place their dominoes however they like. Now, it is considered a violation. According to the rules, the numbers on the ends of the two neighboring dominoes must match each other. This rule can also be described as a set of two requirements:</p>

<ol>
	<li>A player cannot add a domino to the end of the snake if it doesn't contain the matching number.</li>
	<li>The orientation of the newly added domino ensures that the matching numbers are neighbors.</li>
</ol>

<p>For example, consider the following situation:</p>

<p>We have a <code class="java">[3,4],[4,4],[4,2]</code> snake and a <code class="java">[1,2]</code> domino. The domino cannot be added to the left side of the snake because there is no 3 in <code class="java">[1,2]</code>. However, the domino can be added to the right side of the snake because <code class="java">[1,2]</code> contains a 2. If we were to place the domino on the right side of the snake, we would have to reorient it: <code class="java">[3,4],[4,4],[4,2],<strong>[2,1]</strong></code>.<br>
<br>
These two requirements are strict for both the player and the computer.</p>

<p><strong>Objectives</strong></p>

<p>Add the following functionality to your code. When it's a player's turn, the program should:</p>

<ol>
	<li>Verify that the move entered by the player is legal (requirement #1).<br>
	If not, request a new input with the following message: <code class="java">Illegal move. Please try again.</code>.</li>
	<li>Place dominoes with the correct orientation (requirement #2).</li>
</ol>

<p>When it's a computer's turn, the program should:</p>

<ol>
	<li>Try random moves until it finds a legal one.<br>
	<div class="alert alert-primary">A set of possible moves ranges from <code class="java">-computer_size</code> to <code class="java">computer_size</code> (where the <code class="java">computer_size</code> is the number of dominoes the computer still has). Skipping a turn (move 0) is always legal.</div></li>
	<li>Place dominoes with the correct orientation.</li>
</ol>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1</strong></p>

<p><em>Invalid move</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 5]
2:[1, 5]
3:[2, 4]
4:[2, 6]
5:[0, 1]
6:[1, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
&gt; 5
Illegal move. Please try again.
&gt;</code></pre>

<p><strong>Example 2</strong></p>

<p><em>Valid move (with corrected domino orientation)</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
&gt; 7
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][6, 1]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
&gt;</code></pre>



<h1>Stage 5</h1>

<p>Randomly made choices are hardly a sign of intelligence. Teach your computer to make educated decisions with the help of basic statistics. Here's how it works:</p>

<p>The primary objective of the AI is to determine which domino is the least favorable and then get rid of it. To reduce your chances of skipping a turn, you must increase the diversity of your pieces. For example, it's unwise to play your only domino that has a 3, unless there's nothing else that can be done. Using this logic, the AI will evaluate each domino in possession, based on the rarity. Dominoes with rare numbers will get lower scores, while dominoes with common numbers will get higher scores.</p>

<p>The AI should use the following algorithm to calculate the score:</p>

<ol>
	<li>Count the number of 0's, 1's, 2's, etc., in your hand, and in the snake.</li>
	<li>Each domino in your hand receives a score equal to the sum of appearances of each of its numbers.</li>
</ol>

<p>The AI will now attempt to play the domino with the largest score, trying both the left and the right sides of the snake. If the rules prohibit this move, the AI will move down the score list and try another domino. The AI will skip the turn if it runs out of options.</p>

<p><strong>Objectives</strong></p>

<p>Replace the random move generator with the algorithm described above. Let's analyze how the computer will act in two example situations:</p>

<p>1. The first case<strong> </strong>(see Example 1 below).</p>

<pre><code class="language-no-highlight">Computer pieces: [2,5],[3,5],[0,5]
Domino snake: [4,4],[4,2],[2,1],[1,0],[0,0],[0,2]</code></pre>

<p>Count:</p>

<pre><code class="java">0: 5
1: 2
2: 4
3: 1
4: 3
5: 3
6: 0</code></pre>

<p>Scores:</p>

<pre><code class="language-no-highlight">[2,5]: 4 + 3 = 7
[3,5]: 1 + 3 = 4
[0,5]: 5 + 3 = 8
</code></pre>

<p>Attempts:<br>
Domino <code class="java">[0,5]</code> has the highest score. However, it cannot be played at this moment.<br>
Domino <code class="java">[2,5]</code> has the second-highest score. We can play it by appending it to the right side of the snake.</p>

<p>The result:<br>
Play the <code class="java">[2,5]</code> domino by appending it to the right side of the snake.</p>

<p>2.<strong> </strong>The second case (see example 2 below).</p>

<pre><code class="language-no-highlight">Computer pieces: [1,5],[3,5],[0,5]
Domino snake: [4,4],[4,2],[2,1],[1,0],[0,0],[0,2]</code></pre>

<p>Count:</p>

<pre><code class="java">0: 5
1: 3
2: 3
3: 1
4: 3
5: 3
6: 0</code></pre>

<p>Scores:</p>

<pre><code class="language-no-highlight">[1,5]: 3 + 3 = 6
[3,5]: 1 + 3 = 4
[0,5]: 5 + 3 = 8
</code></pre>

<p>Attempts:<br>
Domino <code class="java">[0,5]</code> has the highest score. However, it cannot be played at this moment.<br>
Domino <code class="java">[1,5]</code> has the second-highest score. However, it cannot be played at this moment.<br>
Domino <code class="java">[3,5]</code> is the last option. Unfortunately, it also cannot be played at this moment.</p>

<p>The result:<br>
Take an extra piece from the stock (if it's not empty) and skip a turn.</p>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1</strong></p>

<p><em>The Computer plays a domino.</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 12
Computer pieces: 3

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: Computer is about to make a move. Press Enter to continue...
&gt;
======================================================================
Stock size: 12
Computer pieces: 2

[4, 4][4, 2][2, 1]...[0, 0][0, 2][2, 5]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
&gt;</code></pre>

<p><strong>Example 2</strong></p>

<p><em>The</em><strong> </strong><em>Computer skips the turn.</em></p>

<pre><code class="language-no-highlight">======================================================================
Stock size: 12
Computer pieces: 3

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: Computer is about to make a move. Press Enter to continue...
&gt;
======================================================================
Stock size: 11
Computer pieces: 4

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
&gt;</code></pre>
