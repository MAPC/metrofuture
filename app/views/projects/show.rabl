object @project

attributes :id,
           :title,
           :description,
           :status,
           :lead_department

node(:geographies) { |project| project.geographies } unless locals[:hide_geographies]