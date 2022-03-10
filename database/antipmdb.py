#    This file is part of NiceGrill.

#    NiceGrill is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    NiceGrill is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with NiceGrill.  If not, see <https://www.gnu.org/licenses/>.

from database.mongo import cli
import logging


cli = cli["NiceGrill"]["AntiPM"]


async def set_antipm(opt):
    return cli.insert_one({"AntiPM": opt})

async def approve(user):
    return cli.insert_one({"Approved": user})

async def set_limit(digit):
    return cli.insert_one({"Limit": digit})

async def set_notif(opt):
    return cli.insert_one({"Notifications": opt})

async def set_sblock(opt):
    return cli.insert_one({"SuperBlock": opt})

async def check_antipm():
    return (
        cli.find_one({"AntiPM": {"$exists": True}})["AntiPM"]
        if cli.find_one({"AntiPM": {"$exists": True}})
        else False
    )

async def check_limit():
    return (
        cli.find_one({"Limit": {"$exists": True}})["Limit"]
        if cli.find_one({"Limit": {"$exists": True}})
        else 3
    )
    
async def check_sblock():
    return (
        cli.find_one({"SuperBlock": {"$exists": True}})["SuperBlock"]
        if cli.find_one({"SuperBlock": {"$exists": True}})
        else False
    )

async def check_notifs():
    return (
        cli.find_one({"Notifications": {"$exists": True}})["Notifications"]
        if cli.find_one({"Notifications": {"$exists": True}})
        else True
    )

async def check_approved(user):
    return cli.find_one({"Approved": user})

async def delete(obj):
    return cli.delete_one({obj: {"$exists": True}})

async def disapprove(user):
    return cli.delete_one({"Approved": user})
