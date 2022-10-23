const axios = require('axios');
import baseUrl from './base';

const new = async (routeId, startTime, stopTime,startPoint,stopPoint,buses,passengers) => {
    const r = await axios.patch(`${baseUrl}/routes/new?routeId=`, {
        routeId: routeId}, `&startTime=`,
        {startTime: startTime}, `&stopTime=`,
        {stopTime: stopTime}, `&startPoint=`,
        {startPoint: startPoint},`&stopPoint=`
        {stopPoint: stopPoint}, `&buses=`,
        {buses: buses}, `&passengers=`
        {passengers: passengers}
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

const fromMinute = async (aMinute) => {
    const r = await axios.get(`${baseUrl}/fromMinute?minute=`,{minute: aMinute});

    return r.data.exists;
};

const updateRoads = async (routeId, startTime, stopTime, startPoint, stopPoint) => {
    const r = await axios.patch(`${baseUrl}/routes/routes?routeId=`, {
        routeId: routeId}, `&startTime=`,
        {startTime: startTime}, `&stopTime=`,
        {stopTime: stopTime}, `&startPoint=`,
        {startPoint: startPoint}, `&stopPoint=`,
        {stopPoint: stopPoint}
    );
    if (r.status === 200) {
        return r.data;
    } else {
        throw Error(' error');
    }
};

const delete = async (routeId,busId) => {
    const r = await axios.delete(`${baseUrl}/routes/deleteBus?routeId=`,
        {roadId: roadID}, `&busId=`,
        {busId: busId}

    );
    if (r.status === 200) {
        return r.data;
    } else {
        throw Error(' error');
    }
};

const add_bus = async (routeId,busId) => {
    const r = await axios.delete(`${baseUrl}/routes/addBus?routeId=`,
        {roadId: roadID}, `&busId=`,
        {busId: busId}

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