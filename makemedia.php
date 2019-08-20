#!/usr/bin/php -q
<?php

if ($argc > 1) {
    if (is_dir($argv[1])) {
        // Create media files for a directory, including subdirectories
        $imagedir = findRootDir($argv[1]) . "/source/img/";
        parseDir(dir($argv[1]));
    }
    if (is_file($argv[1])) {
        // Create media for a single file
        $dir = dirname($argv[1]);
        $imagedir = findRootDir($dir) . "/source/img/";
        $config = getConfig(dir($dir));
        $filename = basename($argv[1]);
        if (key_exists($filename, $config)) {
            createMedia(dirname($argv[1]), $filename, $config[$filename]);
        }
        else {
            echo "No config entry for " . $argv[1];
            exit(1);
        }
        
    }
    
} else {
    // Create all media files
    chdir(findRootDir(realpath(".")));
    $dir = dir("./source/qml");
    $imagedir = realpath("./source/img/");
    parseDir($dir);
}
exit(0);

/**
 * Find the root directory of the checked out HIG project
 */
function findRootDir($dir) {
    global $imagepath;
    
    while (is_dir($dir)) {
        if (is_dir($dir . "/source")) {
            return realpath($dir);
        }
        $dir .= "/..";
    }
    echo "Could not find HIG root directory.";
    exit(1);
}

/**
 * Parse a direcotry and its subdirectory
 */
function parseDir(\Directory $dir) {
    $config = getConfig($dir);
    
    while (false !== ($entry = $dir->read())) {
        if (is_dir($dir->path . "/" . $entry)) {
            if ($entry[0] != ".") {
                parseDir(dir($dir->path . "/" . $entry));
            }
        }
        
        if (key_exists($entry, $config)) {
            createMedia($dir->path, $entry, $config[$entry]);
        }
    }
    $dir->close();
}

/**
 * Read the json config file or return an empty config
 */
function getConfig(\Directory $dir) {
    if (is_file($dir->path . "/config.json")) {
        return json_decode(file_get_contents($dir->path . "/config.json"), true);
    }
    return [];
}

/**
 * Create a media file according to the config
 */
function createMedia($path, $filename, $config) {
    global $imagedir;
    $pathinfo = pathinfo($path. "/" . $filename);
    //echo "Changing to " . $path;
    chdir($path);
    echo "Creating media for " . $filename . " ";
    $options = "";
    
    if (isset($config["controls"]) && $config["controls"] == "mobile") {
        putenv("QT_QUICK_CONTROLS_MOBILE=1");
        putenv("QT_QUICK_CONTROLS_STYLE=Plasma");
    }
    else {
        putenv("QT_QUICK_CONTROLS_MOBILE=0");
        putenv("QT_QUICK_CONTROLS_STYLE=org.kde.desktop");
    }
    
    if (isset($config["autostart"])) {
        $options .= " -a " . $config["autostart"];
    }
    
    if (isset($config["scale"]) && is_numeric($config["scale"])) {
        putenv("QT_SCALE_FACTOR=" . $config["scale"]);
    }
    else {
        putenv("QT_SCALE_FACTOR=1");
    }
    
    if (isset($config["fps"])) {
        $options .= " -f " . $config["fps"];
    }
    
    if (isset($config["duration"])) {
        $options .= " -s " . $config["duration"];
    }
    
    switch ($config["type"]) {
        case "png":
            error_log("qmlgrabber " . $filename . $options );
            exec("qmlgrabber " . $filename . $options );
            $output = $imagedir . $pathinfo["filename"] . ".png";
            echo "moving file to " . $output;
            if (is_file($output)) {
                unlink($output);
            }
            rename(realpath($path) . "/Screenshot.png", $output);
        break;
        case "webm":
            echo "qmlgrabber " . $options . " " . $filename . "\n\n";
            exec("qmlgrabber " . $options . " " . $filename);
            exec("ffmpeg -r 60 -f image2 -i Frames/Frame-%d.png -vcodec libvpx -b:v 1M video.webm;");
            $output = $imagedir . $pathinfo["filename"] . ".webm";
            echo "moving file to " . $output;
            if (is_file($output)) {
                unlink($output);
            }
            rename(realpath($path) . "/video.webm", $output);
            exec("rm -r Frames");
        break;
        case "gif":
            exec("qmlgrabber " . $filename . $options);
            exec("ffmpeg  -f image2 -i Frames/Frame-%d.png -vf fps=10,scale=240:-1:flags=lanczos,palettegen palette.png");
            exec('ffmpeg  -f image2 -i Frames/Frame-%d.png -i palette.png -filter_complex "fps=20,scale=240:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif');
            $output = $imagedir . $pathinfo["filename"] . ".gif";
            echo "moving file to " . $output;
            if (is_file($output)) {
                unlink($output);
            }
            rename(realpath($path) . "/output.gif", $output);
            exec("rm -r Frames");
            exec("rm palette.png");
        break;
    }
    echo "\n";
    putenv("QT_QUICK_CONTROLS_MOBILE=0");
    putenv("QT_QUICK_CONTROLS_STYLE=org.kde.desktop");
    putenv("QT_SCALE_FACTOR=1");
}
