# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import os
import sys
import bpy

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir)

from road_base import DSC_OT_road
from geometry import DSC_geometry_clothoid


class DSC_OT_junction_connection(DSC_OT_road):
    bl_idname = 'dsc.junction_connection'
    bl_label = 'Junction connection'
    bl_description = 'Create a connecting road inside a junction'
    bl_options = {'REGISTER', 'UNDO'}

    object_type = 'junction_connecting_road'
    snap_filter = 'OpenDRIVE_junction'
    snapped_only = True

    geometry = DSC_geometry_clothoid()
