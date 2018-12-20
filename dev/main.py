import click 

@click.group()
@click.option('--input_file', 
              type=click.File('r'),
              prompt='ENTER INPUT FILE',
              help='filename to parse')
@click.option('--output_file',
              default = "", 
              type=click.File('w'), 
              help='the filename to write to')
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, input_file, output_file, debug):
    ''' Parser for Executable and Linkable Formatted Files '''
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below
    ctx.ensure_object(dict)

    ctx.obj['DEBUG'] = debug
    ctx.obj['INPUT'] = input_file 
    ctx.obj['OUTPUT'] = output_file if output_file else None  


@cli.command()
@click.pass_context
def tokenize(ctx):
    ''' Pass ELF file to lexer/tokenizer '''
    pass


@cli.command()
@click.pass_context
def segmentize(ctx):
    ''' pretty print the segments of the ELF file '''
    pass


if __name__ == "__main__":
    cli(obj={})
