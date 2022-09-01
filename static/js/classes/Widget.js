/**
 * Abstract Class Widget.
 *
 * @class Widget
 */
export class Widget {

    constructor() {
        if (this.constructor == Widget) {
            throw new Error("Abstract classes can't be instantiated.");
        }
    }

    // Only function to modify for each widget
    __build() {
        return "";
    }

    // Function to add css to widget
    __add_style() {
        return "";
    }
    
    open(json) {
        this.json = json;  // Create global json variable
        var html = this.__build();  // Get the results of the build function
        var style = `<style>${this.__add_style()}</style>`
        html = style.concat(html);
        // Display the build function
        $("#widget-content").fadeOut('slow', function() {
            $("#widget-content").html(html);
            $("#widget-content").fadeIn();
        });

    }
    
}