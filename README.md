# music-database

okay i should preface this by saying this is a tool i made to cater to a very niche inconvenience i was facing so this is probably not of any interest to anyone other than me but! it's fine.

some background: i am a kpop fan (...) and in that industry, the act of composing/writing lyrics for/producing music is often outsourced and relatively inconsistent (exchanging music is more like a business transaction, if there are personal connections between writers, they are pre-existing and it's common for songwriters to have no ties to the company/group at all and just have sold this one song to them). so, i wanted to create a database of some sorts to keep track of who worked my favorite songs in order to easily find connections between songs i enjoy.

this project makes use of the genius API and notion API to accomplish this goal: basically, it allows you to search for a song on genius, then retrieves all the properties of the song.  it picks out writers, producers, and any other credits of your interest, and repackages them in a dictionary. then, it uses the notion API to add that dictionary into a database.

# how to use
{still writing this out sorry -- you can contact me if you want an access token before i get around to writing this. if i'm being honest i genuinely don't think anyone other than me will be using this so i might never get around to it LOL}

the only thing you have to modify is the file called access_token.py: there are two variables within that file, GENIUS_ACCESS_TOKEN and NOTION_ACCESS_TOKEN. 

you need to generate access tokens for both genius and notion and add them to that file.

you also need to create the notion database you want to add to, give this connection permission to modify it, and give the link to music-database
