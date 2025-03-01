import { Layout } from 'antd';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TaskPage from '../components/TaskPage/Index';
import { BottomMenu } from '../components/BottomMenu/Index'
import { TaskDetailPage } from '../components/TaskDetailPage/Index';

const App = () => {
    const { Header } = Layout;

    return (
        <Layout style={{ minHeight: '100vh', padding: '0px', margin: '0px 0px 50px 0px' }}>
            <Router>
                <Routes>
                    <Route path="/" element={<TaskPage />} />
                    <Route path="/task/:id" element={<TaskDetailPage />} />
                </Routes>
            </Router>

            <BottomMenu />
        </Layout>

    );
};

export default App;