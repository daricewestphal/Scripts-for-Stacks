import pandas as pd

def task_process_radtags():

	source1_format = '/Volumes/ExFAT/New_Illumina_Demultiplex/block{}'
	source2_format = '/Volumes/exFAT/New_Illumina_Demultiplex/Barcodes_for_demultiplex/barcodes_block{}.txt'
	dest_format = '/Volumes/exFAT/run_process_radtags_stacks2/results/process_radtags_output_block{}'
	
	bin = 'process_radtags'
	
	individuals = pd.read_table ('infiles/identifiers.txt', header=None, squeeze=True)

	# for i in individuals:	
	for i in individuals:
		
		src1 = source1_format.format(i)
		src2 = source2_format.format(i)
		dest = dest_format.format(i)
		dest_file = '{}/process_radtags.block{}.log'.format(dest, i)
		
		yield {
			'basename': 'process_radtags-{}'.format(i),
			'actions': ["mkdir -p {}".format(dest),
						"{} -P -p {} -b {} -o {} --renz_1 sphI --renz_2 mluCI -E phred33 -c -q --inline_null -i gzfastq -r".format(bin, src1, src2, dest)],
			'file_dep': [src2],
			'targets': [dest_file]
			}
