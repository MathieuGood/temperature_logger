<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8" />
        <!-- <meta name="viewport" content="width=device-width, initial-scale=1" /> -->
        <link rel="stylesheet" href="style.css" />
        <title>Températures</title>
    </head>
    <body>
        <div class="main">

            <div class="temp-block row" id="top-left">
                <span class='name'>{{ name_salon }}<br></span>
                <span class='temp'>{{ temp_salon }}<br></span>
            </div>

            <div class="temp-block" id="top-right">
                <span class='name'>{{ name_ext }}<br></span>
                <span class='temp'>{{ temp_ext }}<br><</span>
            </div>

            <div class="temp-block" id="bottom-left">
                <span class='name'>{{ name_cam }}<br></span>
                <span class='temp'>{{ temp_cam }}<br><</span>
            </div>

            <div class="temp-block" id="bottom-right">
                <span class='name'>{{ name_cl }}<br></span>
                <span class='temp'>{{ temp_cl }}<br></span>
            </div>

        </div>

    </body>
</html>