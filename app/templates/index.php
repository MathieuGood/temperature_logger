<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8" />
        <!-- <meta name="viewport" content="width=device-width, initial-scale=1" /> -->
        <link rel="stylesheet" href="style.css" />
        <title>Températures</title>
    </head>
    <body>
        <?php include('get_temp.php'); ?>
        <div class="main">

            <div class="temp-block row" id="top-left">
                <span class='name'><?php echo $name_salon.'<br />'; ?></span>
                <span class='temp'><?php echo $temp_salon.'°C'; ?></span>
            </div>

            <div class="temp-block" id="top-right">
                <span class='name'><?php echo $name_ext.'<br />'; ?></span>
                <span class='temp'><?php echo $temp_ext.'°C'; ?></span>
            </div>

            <div class="temp-block" id="bottom-left">
                <span class='name'><?php echo $name_cam.'<br />'; ?></span>
                <span class='temp'><?php echo $temp_cam.'°C'; ?></span>
            </div>

            <div class="temp-block" id="bottom-right">
                <span class='name'><?php echo $name_cl.'<br />'; ?></span>
                <span class='temp'><?php echo $temp_cl.'°C'; ?></span>
            </div>

        </div>

    </body>
</html>