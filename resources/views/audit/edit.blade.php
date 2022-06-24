@extends ('layouts.normalPage')
@section('content')

    <body>
        <div class="container text-right m-auto mt-5 ">
            <div class="row ">
                <div class="col-md-3 border ">

                </div>
                <div class="col-md-1 border">
                    <a href="/auditreport"><i class="fas fa-arrow-circle-left fa-3x"></i></a>
                </div>
                <div class="col-md-4 border text-center pt-2">
                    <b>View / Edit</b>

                </div>
                <div class="col-md-1 border  pt-2">
                    <button type="button" class="btn btn-primary"><i class="fas fa-sliders-h"></i></button>
                </div>
                <div class="col-md-3 border  pt-2">

                </div>
            </div>



            <div class="row py-4    ">
                <div class="col-md-3"> </div>




                <div class="col-md-6 border rounded">
                    <form method="post" action="{{ url('update-audit/' . $audits->audit_id) }}">

                        @csrf

                        <input class="form-control form-control-sm" name="months" value="{{ $audits->months }}"></input>
                        <br>
                        <input class="form-control form-control-sm" name="year" value="{{ $audits->year }}"></input>


                        </tbody>


                        </table>
                        <button type="submit" class="btn btn-primary"> Submit </button>
                    </form>

                </div>
                <div class="col-md-3">
                </div>

            </div>




        </div>
        </div>
    </body>
@endsection
