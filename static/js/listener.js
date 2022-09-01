/*
file: listener.js
listener for command changes 
*/

// Imports for widgets
import NewsWidget from "./widgets/NewsWidget.js";
import MusicWidget from "./widgets/MusicWidget.js";

import CommandRunner from "./classes/CommandRunner.js";

var command_runner = new CommandRunner();

// Add widget listeners here!
command_runner.add_command("news", new NewsWidget());
command_runner.add_command("music", new MusicWidget());

// Socket listener, will make connection to localhost, then listen for data in the command channel to be passed
$(document).ready(function() {

    var socket = io.connect('http://127.0.0.1:5000');

    socket.on('connect', function() {
         console.log('connected');
    });
    
    socket.on('command', function(data) {
        command_runner.run_command(data);
    });

});
