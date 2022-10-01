import React from "react";
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as FiIcons from 'react-icons/fi';
import * as FcIcons from 'react-icons/fc';

export const SidebarData = [
{
    title: "Home",
    path: '/',
    icon: <AiIcons.AiFillHome/>,
    cName: 'nav-text'
},
{
    title: "Shifts",
    path: '/shifts',
    icon: <FaIcons.FaArchive/>,
    cName: 'nav-text'
},
{
    title: "Rules",
    path: '/rules',
    icon: <FcIcons.FcRules/>,
    cName: 'nav-text'
},
{
    title: "Settings",
    path: '/settings',
    icon: <FiIcons.FiSettings/>,
    cName: 'nav-text'
},
]
