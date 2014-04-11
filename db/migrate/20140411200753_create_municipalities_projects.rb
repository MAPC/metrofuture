class CreateMunicipalitiesProjects < ActiveRecord::Migration
  def change
    create_table :municipalities_projects, id: false do |t|
      t.belongs_to :municipality
      t.belongs_to :project
    end
    add_index(:municipalities_projects, [:municipality_id, :project_id])
  end
end
