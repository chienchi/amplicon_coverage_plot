#!/usr/bin/env bash
set -e
rootdir=$( cd $(dirname $0) ; pwd -P )
tempdir=$rootdir/tmpOut

test_result(){
	Test=$tempdir/output_amplicon_coverage.txt
	Expect=$rootdir/output.txt
	testName="run test";
	if diff <(tail $Expect) <(tail $Test)
	then
		echo "$testName passed!"
		touch "$tempdir/test.success"
	else
		echo "$testName failed!"
		touch "$tempdir/test.fail"
	fi
}

cd $rootdir
echo "Working Dir: $rootdir";
echo "Running Test ..."

rm -rf $tempdir

$rootdir/../amplicov/amplicov --gff input.gff --bed input.bed --cov coverage.txt --prefix output --outdir $tempdir || true
#$rootdir/../amplicov/amplicov --bed input.bed --cov coverage.txt --prefix output --outdir $tempdir || true

test_result;

