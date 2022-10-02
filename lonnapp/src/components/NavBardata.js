import React from 'react';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as FiIcons from 'react-icons/fi';

export const SidebarData = [
  {
    title: 'Home',
    path: '/',
    icon: <AiIcons.AiFillHome />,
    cName: 'nav-text'
  },
  {
    title: 'Shifts',
    path: '/shifts',
    icon: <IoIcons.IoIosPaper />,
    cName: 'nav-text'
  },
  {
    title: 'Rules',
    path: '/rules',
    icon: <FiIcons.FiBookOpen />,
    cName: 'nav-text'
  },
  {
    title: 'Settings',
    path: '/settings',
    icon: <FiIcons.FiSettings />,
    cName: 'nav-text'
  }
];