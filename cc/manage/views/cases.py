# Case Conductor is a Test Case Management system.
# Copyright (C) 2011-2012 Mozilla
#
# This file is part of Case Conductor.
#
# Case Conductor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Case Conductor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Case Conductor.  If not, see <http://www.gnu.org/licenses/>.
"""
Manage views for cases.

"""
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from django.contrib.auth.decorators import login_required, permission_required

from ...core.sort import sort
from ...library.models import CaseVersion

from ..forms.cases import AddCaseForm



@login_required
@sort("caseversions")
def cases(request):
    return TemplateResponse(
        request,
        "manage/product/testcase/cases.html",
        {
            "caseversions": CaseVersion.objects.all(), # @@@ just latest?
            }
        )



@permission_required("library.create_cases")
def add_case(request):
    if request.method == "POST":
        form = AddCaseForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("manage_cases")
    else:
        form = AddCaseForm(user=request.user)
    return TemplateResponse(
        request,
        "manage/product/testcase/add_case.html",
        {
            "form": form
            }
        )
