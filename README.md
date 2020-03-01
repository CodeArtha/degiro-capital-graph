# degiro-capital-graph
graphs your capital at the end of each trading day to follow the evolution of your portfolio overtime.

commands [wip]
- dg-graph.py fetch : go fetch the capital on degiro if weekday and past setup market closure time
- dg-graph.py export : export the data to csv
- dg-graph.py table : shows the logged data as a table
- dg-graph.py graph : shows the logged data as a graph
- dg-graph.py config --endtime <0000-2359> : configures the market closure time to your timezone and traded market
- dg-graph.py config --dguser <username> : sets your degiro username
- dg-graph.py config --dgpass <password> : sets your degiro password
- dg-graph.py config --dgpassfile <path> : sets the path to a file in which you store your degiro password

Safety Note: on gnome/xfce/kde based linux systems the username and passwords are stored in the gnome-keyring. To avoid your password from appearing in your command history you can set the password to a dummy one and then go edit it manually in the gnome-keyring app.
