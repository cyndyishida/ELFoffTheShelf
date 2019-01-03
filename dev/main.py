import click 
from hex_ascii import ( 
    HEX_OFFSET, 
    HEX_TO_ASCII,
    HEX_UNIT, 
    serialize_hex_and_ascii, 
    clean_ascii,
)

SPACE = "  "


    
@click.group()
@click.option('--input_file', 
              type=click.File('rb'),
              prompt='ENTER INPUT FILE',
              help='filename to parse')
@click.option('--output_file',
              default = "", 
              type=click.File('w'), 
              help='the filename to write to')
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, input_file, output_file, debug):
    ''' Parser for Executable and Linkable Formatted Files on Mac OS'''
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below
    ctx.ensure_object(dict)

    ctx.obj['DEBUG'] = debug
    ctx.obj['INPUT'] = [input_file.read()]
    ctx.obj['OUTPUT'] = output_file if output_file else None  


@cli.command()
@click.pass_context
def hexdump(ctx):
    ''' Pretty print hex representation of file.'''
    x = ctx.obj['INPUT']
    output = []
    start = hex(0)
    for section in x: 
        sect = str(section.hex())
        # limit HEX_UNIT * 2 chars on each line 
        for i in range(0, len(sect), HEX_UNIT *2): 
            hex_line = f"{start.ljust(HEX_OFFSET)}{SPACE}"
            # first half 
            curr_parsed = serialize_hex_and_ascii(i, i+HEX_UNIT, sect) 
            hex_line += curr_parsed[0]
            ascii_line = curr_parsed[1]
            hex_line += SPACE
            # second half 
            curr_parsed = serialize_hex_and_ascii(i+HEX_UNIT, i+HEX_UNIT*2, sect) 
            hex_line += curr_parsed[0] 
            ascii_line += curr_parsed[1]
            ascii_line = clean_ascii(ascii_line)
            start = hex(int(start, HEX_UNIT)+0x01) # increment line counter 
            output.append(hex_line.ljust(58)+ascii_line.rjust(20))
        output.append(f"{'*'.ljust(HEX_OFFSET)}{SPACE}")
    output.pop()
    print("\n".join(output))
        

@cli.command()
@click.pass_context
def segmentize(ctx):
    ''' pretty print the segments of the file '''
    pass

@cli.command()
@click.argument('segment')
@click.pass_context
def get_segment(ctx, segment):
    ''' pretty print the specified segment of the file '''
    pass

if __name__ == "__main__":
    cli(obj={})
