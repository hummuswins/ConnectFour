# ConnectFour
Either an AI Game or Self-Played Connect Four game using the server at UCI

The program

For this project, you'll implement a console-based game that you will initially be able to play on your own computer, but will extend so that you can play via the Internet by connecting to a central, shared server.

The game

For this project, you'll implement a console-based implementation of a game called Connect Four. The rules of the game are straightforward and many of you may already know them; if you're not familiar with the rules of the game, or haven't seen them in a while, Wikipedia's Connect Four page is as good a place to go as any to become familiar with it.

Note that our implementation will include not only the traditional rules regarding dropping pieces into columns, but also the "Pop Out" variation discussed on the Wikipedia page. While Connect Four boards come in a variety of sizes, our implementation will default to 7x6 (i.e., seven columns and six rows).

Also, one very minor wrinkle that we're adding to the rules on the Wikipedia page is that the red player always moves first.

A starting point: the connectfour module

Unlike the previous project, this project begins with a starting point, in the form of a library that I've already implemented that contains the underlying game logic. You will be required to build your game on top of it (and you will not be allowed to change it), which will be an instructive experience; learning to use other people's libraries without having to make modifications (and, in a lot of cases, without being allowed to make them) is a valuable real-world programming ability. Before proceeding much further with the project, it might be a good idea to spend some time reading through the code, its docstrings, and its comments to get an understanding of what's been provided. You can also try some focused experimentation in the Python interpreter so you can understand how the provided module works; you'll need that understanding in order to complete your work. Don't worry if not all of it makes complete sense initially, but do get a feel for what's available at the outset, then gradually fill in the details as you move forward.

The Connect Four game logic is linked below:

connectfour.py
Be sure that you respect the constants that are defined in this module. For example, whenever possible, use connectfour.BOARD_COLUMNS to denote the number of columns on the board, connectfour.BOARD_ROWS to denote the number of rows on the board, and so on. It should be possible to change the values of these constants to reasonable alternative values and your program should still work (and should adjust if, for example, the number of columns and rows changes).

The requirements

You will actually be writing two programs to satisfy this project's requirements. The vast majority of the code will be shared between the two programs. In fact, one of your goals is to find a way to reuse as much of it as possible; if you find yourself copying and pasting code between the programs, you should instead consider a way to use the put the code in one place and use it in both.

The first program: a console-only version of Connect Four

One of your two programs will allow you to play one game of Connect Four using only console interaction (i.e., no networks or sockets). The user is repeatedly shown the current state of the game — whose turn it is and what the board looks like. The board should always be shown in the following format:

1  2  3  4  5  6  7
.  .  .  .  .  .  .
.  .  .  .  .  .  .
.  .  .  .  .  .  .
.  .  R  .  .  .  .
.  .  Y  R  .  .  .
.  R  R  Y  .  Y  .
You have some latitude in how you ask the user to specify a move, but it needs to be clear what the user should do. Do not assume that your user will know what to type; tell them (briefly). Columns should be selected by typing a number between 1 (the far-left column) and 7 (the far-right).

When the user is asked to specify a move but an invalid one is specified (such as dropping into a column that is full), an error message should be printed and the user should be asked again to specify a move. In general, erroneous input at the console should not cause the program to crash; it should simply cause the user to be asked to specify his or her move again.

The game proceeds, one move at a time, until the game ends, at which point the program ends.

The second program: a networked version of Connect Four

Your second program will instead allow you to play a game of Connect Four via a network, by connecting to a server that I've provided. Your program always acts as a client.

When this program starts, the user will need to specify the host (either an IP address, such as 192.168.1.101, or a hostname, such as www.ics.uci.edu) where a Connect Four server is running, along with the port on which that server is listening.

Additionally, the user should be asked to specify a username. The username can be anything the user would like, except it cannot contain whitespace characters (e.g., spaces or tabs). So, for example, boo or HappyTonight are legitimate usernames, but Hello There is not.

Once the user has specified where to connect, the program should attempt to connect to the server. If the connection is unsuccessful, print an error message specifying why and end the program. If, on the other hand, the connection is successful, the game should proceed, with the client acting as the red player (and moving first) and the server — which acts as an artificial intelligence — acting as the yellow player. For red player moves, the user should specify the move at the console, as in your first program; for yellow player moves, the program should instead communicate with the server and let the server determine what move should be made.

As in the first program, the game proceeds, one move at a time, until the game ends, at which point the program ends.

Where is the ICS 32 Connect Four server?

Information about where the server is running will be distributed via email; I'll also keep you posted about planned downtime (e.g., if I need to fix a problem, if I know that the machine where it's running will be down, etc.). It may be necessary to move the server from time to time; when I do that, I will let everyone know via email.

Please note that the ICS 32 Connect Four server is running on a machine on the ICS network that is not exposed to the open Internet. In order to connect to it, you will need to be connected to the campus network, which means you'll either need to be on campus or you'll need to be connected to something called the campus VPN, which allows you to access the campus' network from off-campus. Note, also, that certain residential areas are not connected to a part of the campus network that will allow you direct access to the ICS 32 Connect Four server, so you'll need to use the campus VPN in those cases. In general, if you're not able to connect to the ICS 32 Connect Four server, the first thing you should try is using the campus VPN.

Connecting to the campus VPN requires that you install some software, which you can obtain from UCI's Office of Information Technology at the following link:

Campus VPN software
Open the link above, find the section titled VPN Software (as opposed to WebVPN, which won't work for this purpose), and click the link titled Download the VPN Software. This will require you to log in with your UCInetID and password, at which point you'll be offered links to Windows, Mac OS X, or Linux versions of the VPN software. Download the one that's appropriate for your operating system and install it; instructions for setting it up are available from that page, as well.

