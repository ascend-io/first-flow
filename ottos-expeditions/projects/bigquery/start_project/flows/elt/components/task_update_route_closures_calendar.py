from ascend.resources import task, ref

@task(dependencies=[ref("route_closures")])
def task_update_route_closures_calendar(route_closures, context):
  # add your Task logic here, you can reference name for this component by using context.component_name
  context.ibis.create_table(context.component_name, route_closures, overwrite=True)
