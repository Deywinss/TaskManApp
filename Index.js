import React from 'react';
import { Menu, Row, Col } from 'antd';
import { AppstoreOutlined, ControlFilled, ScheduleOutlined } from '@ant-design/icons';
import './style.css';

export const BottomMenu = () => {
    const [current, setCurrent] = React.useState('functions');

    const onClick = (e) => {
        setCurrent(e.key);
    };

    return (
        <Row justify="space-around"
            align="middle"
            className='bottom-menu'
        >
            <Col>
                <Menu
                    onClick={onClick}
                    selectedKeys={[current]}
                    mode="horizontal"
                    style={{ width: '100%', justifyContent: 'space-around' }}
                >
                    <Menu.Item key="functions">
                        <div className="menu-item-content">
                            <span> <ControlFilled style={{ fontSize: '30px' }} /></span>
                            <span>Функции</span>
                        </div>

                    </Menu.Item>
                    <Menu.Item key="productivity">
                        <div className="menu-item-content">
                            <span> <AppstoreOutlined style={{ fontSize: '30px' }} /></span>
                            <span>Продуктивность</span>
                        </div>
                    </Menu.Item>
                    <Menu.Item key="plan" >
                    <div className="menu-item-content">
                            <span> <ScheduleOutlined style={{ fontSize: '30px' }} /></span>
                            <span>План</span>
                        </div>
                    </Menu.Item>
                </Menu>
            </Col>
        </Row>
    );
};
