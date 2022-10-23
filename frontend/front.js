const axios = require('axios');
import baseUrl from './base';

const new = async (routeID, startTIME, stopTIME,startPOINT,stopPOINT,Abuses) => {
    const r = await axios.patch(`${baseUrl}/routes/new?routeId=`, {
        routeId: routeID}, `&startTime=`,
        {startTime: startTIME}, `&stopTime=`,
        {stopTime: stopTIME}, `&startPoint=`,
        {startPoint: startPOINT},`&stopPoint=`
        {stopPoint: stopPOINT}, `&buses=`,
        {buses: Abuses}, `&passengers=`
        {passengers: Apassengers}
    );
    if (r.status === 200) {
        return r.data;
    } else {
        throw Error(' error');
    }
};

const schedule = async (schedule) => {
    const r = await axios.get(`${baseUrl}/schedule`);

    return r.data.exists;
};

const fromMinute = async (Aminute) => {
    const r = await axios.get(`${baseUrl}/fromMinute?minute=`,{minute: Aminute});

    return r.data.exists;
};

const updateroads = async (routeID, startTIME, stopTIME, startPOINT, stopPOINT) => {
    const r = await axios.patch(`${baseUrl}/routes/routes?routeId=`, {
        routeId: routeID}, `&startTime=`,
        {startTime: startTIME}, `&stopTime=`,
        {stopTime: stopTIME}, `&startPoint=`,
        {startPoint: startPOINT}, `&stopPoint=`,
        {stopPoint: stopPOINT}
    );
    if (r.status === 200) {
        return r.data;
    } else {
        throw Error(' error');
    }
};

const delete = async (routeID,busID) => {
    const r = await axios.delete(`${baseUrl}/routes/deleteBus?routeId=`,
        {roadId: roadID}, `&busId=`,
        {busId: busID}

    );
    if (r.status === 200) {
        return r.data;
    } else {
        throw Error(' error');
    }
};

const add_bus = async (routeID,busID) => {
    const r = await axios.delete(`${baseUrl}/routes/addBus?routeId=`,
        {roadId: roadID}, `&busId=`,
        {busId: busID}

    );
    if (r.status === 200) {
        return r.data;
    } else {
        throw Error(' error');
    }
};



module.exports = {
    new,
    get_day,
    schedule,
    fromMinute
    updateroads,
    delete,
    add_bus


};