/*
 *   Copyright 2018 Fabian Riethmayer
 *
 *   This program is free software; you can redistribute it and/or modify
 *   it under the terms of the GNU Library General Public License as
 *   published by the Free Software Foundation; either version 2, or
 *   (at your option) any later version.
 *
 *   This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU Library General Public License for more details
 *
 *   You should have received a copy of the GNU Library General Public
 *   License along with this program; if not, write to the
 *   Free Software Foundation, Inc.,
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

import QtQuick 2.6
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.2
import org.kde.kirigami 2.4 as Kirigami

Kirigami.ScrollablePage {
    property alias currentIndex: list.currentIndex;
    property var pagemodel;
    property var pageroot;

    Kirigami.Theme.colorSet: Kirigami.Theme.View
    title: pagemodel.name
    id: page

    background: Rectangle {
        color: Kirigami.Theme.backgroundColor
    }

    /*header: Rectangle {
        clip: true
        id: header
        color: "#3daee9"
        height: searchField.implicitHeight + 2 * Kirigami.Units.largeSpacing
        width: root.width
        //border.width: 1
        //border.color: "#bdc3c7"

        TextField {
            id: searchField
            placeholderText: "Search"
            anchors.centerIn: parent
            anchors.margins: Kirigami.Units.largeSpacing
            width: parent.width - 2 * Kirigami.Units.largeSpacing
        }
    }*/

    ListView {
        currentIndex: -1
        id: list
        model: pagemodel.subfolder

        delegate: Kirigami.BasicListItem {
            onClicked: {
                pageroot.pageStack.push(Qt.resolvedUrl("Folder.qml"), {"pagemodel": pagemodel.subfolder.get(index), "pageroot": pageroot});
            }

            contentItem: Row {
                spacing: 2 * Kirigami.Units.largeSpacing

                Item {
                    width: Kirigami.Units.iconSizes.medium
                    height: width

                    Kirigami.Icon {
                        width: Kirigami.Units.iconSizes.medium
                        height: width
                        source: model.icon
                    }
                }
                Label {
                    anchors.verticalCenter: parent.verticalCenter
                    text: model.name
                }
            }
        }
    }
}
