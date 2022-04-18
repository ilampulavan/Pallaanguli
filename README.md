# Pallaanguli
Code for the Tamilnadu (India) traditional game Pallaanguli...
It spelled in Tamil as பல்லாங்குழி, in English it spelled sometimes as Pallanguli / Pallanguzhi.
There are many variations to this game in all over south India.
However the following rules and set-ups are considered for this version of the game.
Wikipedia link: 
for Tamil: https://ta.wikipedia.org/wiki/%E0%AE%AA%E0%AE%B2%E0%AF%8D%E0%AE%B2%E0%AE%BE%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AF%81%E0%AE%B4%E0%AE%BF
for English: https://en.wikipedia.org/wiki/Pallanguzhi

SET-UP:
1. It should be played by exactly 2 players.
2. There are 14 holes in total and 7 for each player.
3. Each player has 35 'CHOLIS' (Tamil spelling சோளி). But I called them as coins in the code and here onwards.
4. Each hole should be filled initially with 5 coins.

RULES:
1. The player who starts the game, usually is chosen by tossing or similar. This is not implemented in this version. Whoever plays first is called Player 1.
2. The holes are numbered from the left side of the Player 1.
3. The next hole is determined circularly. If the hole is 14, the next holes is 1. In the code hole index starts from 0.

STEPS:
1. A player can choose any hole from his holes which has coins.
2. He/She takes all the coins from the chosen hole.
3. Those coins will be distributed next holes by single coin until the coins remain.
4. And if the next hole has coins, then he will remove the coins & distributes as above to next holes.
5. But if the next hole is empty where he needs to take, then the turn ends. The hole which is next to the empty one is win-hole. And he/she will take out the coins from the hole.
6. And he/she will keep the coins with him as his score.
7. While distributing the coins, whenever a hole reaches 4 coins [(5-1) coins], the owner of the hole will take out the coins & keep with him/her. This is called 'PASU'.
8. This ends when a current player has no holes with coins.
9. Accourding to the scores of the players, the next round starts & the coins filled again in the holes, 5 each. If a player does not have the coins to fill the hole, then the hole will not be used for the round.
10. The round ends when one of the players does not have the coins to fill even single hole i.e 5 coins. So the player looses the game. Hence the another player wins the game.

