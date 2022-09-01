
import {Widget} from "../classes/Widget.js"
/**
 * NewsWidget, get updated news and display them
 *
 * @class NewsWidget
 * @extends {Widget}
 */
export default class NewsWidget extends Widget {

    __build() {
         
        var headlines = "";

        for (var headline in this.json['data']) {

            var headline_html = `
            <div class='headline-container'>
                <div class='headline-icon'><img src='/static/assets/News.png'></div>
                <div class='headline-text'>${headline}</div>
            </div>
            `
            headlines = headlines.concat(headline_html)
            
        }

        var html = `
        <div class='app-main-container'>
            <div class='news-app-container'>
                ${headlines}
            </div>
        </div>
        `;

        console.log("Opening news app!");

        return html;
    }

    __add_style() {
        var styles = `
        .news-app-container {
            border: 1px solid white;
            text-align: left;
            font-size: 18px;
            width: 600px;
            padding-top: 30px;
            padding-left: 30px;
            border-radius: 20px;
            margin-left: auto;
            margin-right: auto;
        }

        .headline-container {
            height: 70px;
        }

        .headline-icon {
            float: left;
        }

        .headline-icon img {
            width: 40px;
            height: 40px;
        }

        .headline-text {
            float: left;
            margin-left: 20px;
            margin-top: 10px;
            max-width: 500px;
            white-space: nowrap;
            overflow-x: hidden;
        }
        `;
        return styles;
    }

}