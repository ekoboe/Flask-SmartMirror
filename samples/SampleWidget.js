
/*
** This is a sample template for modular widget implementation **
Steps for implementation:
1) Add this file to /static/js/widgets/ folder
2) After creating python backend, create the front end in two steps.
3) Add parsing into __build function, the python json sent via CommandHandler is inherited by this.json variable
4) Add neccesary css styling to the __add_style function
5) Add definition to listener.js in /static/js/listener.js, add it to command_runner.add_command(key, new SampleWidget());
*/


import {Widget} from "../classes/Widget.js"
/**
 * NewsWidget, get updated news and display them
 *
 * @class NewsWidget
 * @extends {Widget}
 */
export default class SampleWidget extends Widget {

    __build() {  // Add design here by parsing python json you sent via CommandHandler
        console.log(this.json);
        var html = "<b>Hello World!</b>";
        return html;
    }

    __add_style() {  // Add css styling here
        var styles = `
        .example {
            color: red;
        }
        `;
        return styles;
    }

}