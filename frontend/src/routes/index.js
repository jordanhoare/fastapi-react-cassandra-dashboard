import { useRoutes } from 'react-router-dom';
import { lazy } from 'react';


import MainLayout from 'layout/MainLayout';

const DashboardDefault = lazy(() => import('../pages/dashboard'));
const SamplePage = lazy(() => import('../pages/extra-pages/SamplePage'));
const Typography = lazy(() => import('../pages/components-overview/Typography'));
const Color = lazy(() => import('../pages/components-overview/Color'));
const Shadow = lazy(() => import('../pages/components-overview/Shadow'));
const AntIcons = lazy(() => import('../pages/components-overview/AntIcons'));


export default function ThemeRoutes( {cars} ) {
    return useRoutes([
        
        {
            path: '/',
            element: <MainLayout cars = {cars} />,
            children: [
                {
                    path: '/',
                    element: <DashboardDefault cars = {cars} />
                },
                {
                    path: 'color',
                    element: <Color />
                },
                {
                    path: 'dashboard',
                    children: [
                        {
                            path: 'default',
                            element: <DashboardDefault cars={cars}/>
                        }
                    ]
                },
                {
                    path: 'sample-page',
                    element: <SamplePage cars={cars} />
                },
                {
                    path: 'shadow',
                    element: <Shadow />
                },
                {
                    path: 'typography',
                    element: <Typography />
                },
                {
                    path: 'icons/ant',
                    element: <AntIcons />
                }
            ]
        }]);
}
