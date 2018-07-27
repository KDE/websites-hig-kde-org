var ruler = Qt.createComponent("Ruler.qml");
var brace = Qt.createComponent("Brace.qml");
var outline = Qt.createComponent("Outline.qml");
var messure = Qt.createComponent("Messure.qml");
var padding = Qt.createComponent("Padding.qml");

// get classname and strip _QML of the name
function getClassName(obj) {
    var str = obj.toString();
    str = str.substring(0, str.indexOf("("));
    if (str.search(/_QML/) !== -1) {
        str = str.substring(0, str.indexOf("_QML"));
    }
    return str.toLowerCase();
}

// An extended array of QML elements
function An(node) {
    this.nodes = [];
    if (typeof node === "undefined") {
        this.nodes = []
    }
    else if (typeof node === "Array") {
        this.nodes = node;
    }
    else {
        this.nodes = [node];
    }
}

// Find an An of QML elements from this point down the subtrees
An.prototype.find = function(selector) {
    var result = new An();

    if (typeof selector === "string") {
        selector = new Select(selector);
    }

    /* for debugging
    for (var member in this) {
        if (typeof this[member] !== "function") {
            console.log(member + ": " + this[member]);
        }
    }*/

    // iterate threw the children
    // apply the selector and traverse down the tree
    for (var n = 0; n < this.nodes.length; n++) {
        var node = this.nodes[n];
        for (var i = 0; i < node.children.length; i++) {
            if (selector.match(node.children[i])) {
                // Add matching element to result
                result.nodes.push(node.children[i]);
            }
            if (node.children[i].children.length) {
                // Merge matching results of subrtree
                var child = new An(node.children[i]);
                result.concat(child.find(selector));
            }
        }
    }
    return result;
}

// Search only direct children
An.prototype.children = function(selector) {
    var result = new An();

    if (typeof selector === "string") {
        selector = new Select(selector);
    }

    for (var n = 0; n < this.nodes.length; n++) {
        var node = this.nodes[n];
        for (var i = 0; i < node.children.length; i++) {
            if (selector.match(node.children[i])) {
                 // Add matching element to result
                result.nodes.push(node.children[i]);
            }
        }
    }
    return result;
}

An.prototype.concat = function(n) {
    this.nodes = this.nodes.concat(n.nodes);
}

An.prototype.first = function() {
    if (this.nodes.length > 0) {
        return new An(this.nodes[0]);
    }
    return new An();
}

An.prototype.last = function() {
    if (this.nodes.length > 0) {
        return new An(this.nodes[this.nodes.length - 1]);
    }
    return new An();
}

An.prototype.eq = function(n) {
    if (this.nodes.length > n) {
        return new An(this.nodes[n]);
    }
    return new An();
}


/**
 * Draw a tree of all the elements
 */
An.prototype.tree = function(lvl) {
    if (typeof lvl === "undefined") {
        lvl = ""
    }

    /* for debug
    for (var member in this.nodes) {
        if (typeof this[member] !== "function") {
            console.log("|" + lvl + "  " + member + ": " + (typeof this[member]));
        }
    }*/

    for (var n = 0; n < this.nodes.length; n++) {
        var node = this.nodes[n];
        console.log("|" + lvl + "  " + getClassName(node) + "  " + node.toString());
        for (var i = 0; i < node.children.length; i++) {
            var child = new An(node.children[i]);
            child.tree(lvl + "--");
        }
    }
}

/**
 * Drawing annotation on the nodes
 */
An.prototype.draw = function(obj) {
    console.log(this.nodes)
    for (var n = 0; n < this.nodes.length; n++) {
        var node = this.nodes[n];
        var opt;
        for (var type in obj) {
            if (Array.isArray(obj[type])) {
                for (var i = 0; i < obj[type].length; i++) {
                    this._draw(node, type, obj[type][i]);
                }
            }
            else {
                this._draw(node, type, obj[type]);
            }
        }
    }
    return this;
}

/**
 * Internal method to draw
 */
An.prototype._draw = function(node, type, opt) {
    //console.log("drawing " + type)
    switch (type) {
        case "outline":
            outline.createObject(root, {item: node, label: opt.label, aspectratio: opt.aspectratio});
        break
        case "ruler":
            ruler.createObject(root, {rx: node.mapToItem(null, 0, 0).x, horizontal: false});
        break
        case "padding":
            padding.createObject(root, {item: node});
        break
        case "brace":
            brace.createObject(root, {"from": node, "to": opt.to.nodes[0], "text": opt.text, "center": opt.center, "horizontal": opt.horizontal});
        break
        case "messure":
            messure.createObject(root, {"from": node, "to": opt.to.nodes[0], "type": opt.type});
        break
    }
}

/**
 * Selector for qml elements
 */
function Select(str) {
    // TODO support more complex syntax
    // - multiple nodenames, hirachy, ...
    if (str.search(/\{/) !== -1) {
        this.nodeName = str.substring(0, str.indexOf("{"));
        var members = str.match(/\{.+\}/);
        try {
            this.attrs = JSON.parse(members[0]);
        }
        catch(e) {
            console.log("Could not parse attributes");
            console.log(e);
        }
    }
    else {
        this.nodeName = str;
    }
}

/**
 * Check if the node matches the selector
 */
Select.prototype.match = function(node) {
    if (this.nodeName === "*" || getClassName(node) === this.nodeName) {
        if (typeof this.attrs !== "undefined") {
            // TODO only return true if all attributes match
            for (var attr in this.attrs) {
                if (typeof node[attr] !== "undefined" && node[attr].toString() === this.attrs[attr]) {
                    return true;
                }
            }
        }
        else {
            return true;
        }
    }
    return false;
}