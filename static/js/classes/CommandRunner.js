/**
 * Class CommandRunner.
 *
 * @class CommandRunner
 */
export default class CommandRunner {

    // Create commands dictionary for sorting command types
    constructor() {
        this.commands = {"open" : {}, "close": "closing"};
    }

    add_command(key, widget) {
        this.commands["open"][key] = widget;
    }

    run_command(json) {
        var key = Object.keys(json)[0];

        console.log(`Running ${key} command!`);
        
        // Switch structure to sort types of commands
        switch(key) {
            case "open":
                this.commands["open"][json[key]].open(json);  // Open the app with inherited open class
                break;
            case "close":
                this.clear_window();  // Clear the window
                break;
        }
    }

    // Clear whatever is in the widget-content frame
    clear_window() {
        $("#widget-content").fadeOut('slow', function() {
            $("#widget-content").html("");
        });
    }

}

