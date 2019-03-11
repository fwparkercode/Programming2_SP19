'''
Below is a list of the top 100 scorers in NBA history.  (I need to update it as it is a year old)
It is a 2d list  [[Name, points], [Name, points]...].
The list is randomized.  

Part 1 (10pts)
Use techniques from this chapter (you choose the method, SELECTION or INSERTION) to SORT the list by POINTS SCORED.
You will need to sort nba_leader_list[i] by using the score located at nba_leader_list[i][1].
You will have to adapt your function to make it work.
This is designed to test your understanding of the sort by applying it to slightly more messy list.  
Solving malformed problems leads to deeper understanding.

Part 2 (5pts)
Now sort the original list using the built in sorted() function or .sort() method.
'''

nba_leader_list = [['Latrell Sprewell', 16712], ['Walter Davis', 19521], ['Kevin Garnett', 26071], ['Mitch Richmond', 20497], ['Magic Johnson', 17707], ['Elvin Hayes', 27313], ['Elgin Baylor', 23149], ['John Havlicek', 26395], ['Dirk Nowitzki', 29907], ['Dwyane Wade', 21139], ['Patrick Ewing', 24815], ['John Stockton', 19711], ['Clifford Robinson', 19591], ['Tom Chambers', 20049], ['Bob Pettit', 20880], ['Tiny Archibald', 16481], ['Adrian Dantley', 23177], ['Walt Bellamy', 20941], ['Dale Ellis', 19004], ['Alex English', 25613], ['Dave Bing', 18327], ['Rolando Blackman', 17623], ['Paul Pierce', 26364], ['Ray Allen', 24505], ['Tracy McGrady', 18381], ['Joe Johnson', 19795], ['Chet Walker', 18831], ['Chris Mullin', 17911], ['Kobe Bryant', 33643], ['Jason Kidd', 17529], ['Chris Webber', 17182], ['Steve Nash', 17387], ['Julius Erving', 30026], ['Bob Cousy', 16960], ['Grant Hill', 17137], ['Tim Duncan', 26496], ['David Robinson', 20790], ['Jeff Malone', 17231], ['Dolph Schayes', 18438], ['Dominique Wilkins', 26668], ['LeBron James', 28178], ['Chris Bosh', 17189], ['Bob Lanier', 19248], ['Artis Gilmore', 24941], ['Dan Issel', 27482], ['Lenny Wilkens', 17772], ['Glen Rice', 18336], ['Reggie Theus', 19015], ['Kevin Willis', 17253], ['Jamal Crawford', 17770], ['Larry Bird', 21791], ['Tony Parker', 18341], ['Pau Gasol', 19666], ['Moses Malone', 29580], ['Kevin Durant', 19008], ['Carmelo Anthony', 23805], ['Terry Cummings', 19460], ['Vince Carter', 24371], ['Shawn Marion', 17700], ['Otis Thorpe', 17600], ['Jason Terry', 18577], ['Reggie Miller', 25279], ['Charles Barkley', 23757], ['Antawn Jamison', 20042], ['Bernard King', 19655], ['Lou Hudson', 17940], ['Wilt Chamberlain', 31419], ['Earl Monroe', 17454], ['Clyde Drexler', 22195], ['Kevin McHale', 17335], ['Gail Goodrich', 19181], ['Hakeem Olajuwon', 26946], ['World B Free', 17955], ['Michael Finley', 17306], ['Jack Sikma', 17287], ['Bob McAdoo', 18787], ['Buck Williams', 16784], ['Scottie Pippen', 18940], ['George McGinnis', 17009], ['Isiah Thomas', 18822], ['Rick Barry', 25279], ["Shaquille O'Neal", 28596], ['George Gervin', 26595], ['Jerry West', 25192], ['Kareem Abdul Jabbar', 38387], ['Karl Malone', 36928], ['Eddie Johnson', 19202], ['Allen Iverson', 24368], ['Mark Aguirre', 18458], ['Zach Randolph', 17399], ['Michael Jordan', 32292], ['Spencer Haywood', 17111], ['Oscar Robertson', 26710], ['Gary Payton', 21813], ['Hal Greer', 21586], ['Robert Parish', 23334], ['Ron Boone', 17437], ['Bailey Howell', 17770], ['Calvin Murphy', 17949], ['Elton Brand', 16827]]
